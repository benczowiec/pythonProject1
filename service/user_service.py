from typing import Set

from sqlmodel import Session, select

from controller.dummy_connector import DummyConnector
from databese.database import engine
from domain.dao.user import User
from domain.dto.user_dto import UserDto
from mappers.user_mapper import UserMapper


class UserService:
    user_endpoint = "users"

    def __init__(self):
        self.user_controller = DummyConnector()
        self.user_mapper = UserMapper()

    def process_users(self, users):
        processed_users: Set[User] = set()
        for user in users:
            new_user: UserDto = UserDto(user["firstName"], user["lastName"],
                                        user["address"]["coordinates"]["lat"],
                                        user["address"]["coordinates"]["lng"])
            new_user.find_localization()
            processed_users.add(self.user_mapper.map_user_to_entity(new_user))
        self.save_users(processed_users)

    def paginate_and_process(self, num_pages, limit):
        skip = 0
        for i in range(num_pages):
            data = self.user_controller.get_data(skip, limit, self.user_endpoint)
            self.process_users(data["users"])
            skip += limit

    def save_users(self, users: set[User]):
        with Session(engine) as session:
            session.add_all(users)
            session.commit()

    def find_all_users(self):
        with Session(engine) as session:
            statement = select(User)
            results = session.exec(statement)
            all_users = results.all()
            return all_users
