from collections import Counter
from typing import Set, Dict

from sqlmodel import Session, select

from controller.dummy_connector import DummyConnector
from databese.database import engine
from domain.dao.dao_all import User, Basket
from domain.dto.user_dto import UserDto
from mappers.user_mapper import UserMapper
from service.product_service import ProductService


class UserService:
    user_endpoint = "users"

    def __init__(self):
        self.user_controller = DummyConnector()
        self.user_mapper = UserMapper()
        self.product_service = ProductService()

    def process_users(self, users):
        processed_users: Set[User] = set()
        for user in users:
            new_user: UserDto = UserDto(user["id"], user["firstName"], user["lastName"],
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

    def find_favorite_categories_for_users(self) -> Dict[int, str]:
        favorite_categories = {}

        with Session(engine) as session:
            users = self.find_all_users()
            for user in users:
                user_id = user.id
                user_name = user.first_name + " " + user.last_name

                statement = select(Basket).where(Basket.user_id == user_id)
                baskets = session.exec(statement).all()

                product_ids = [basket.product_id for basket in baskets]
                products = self.product_service.find_all_products_by(product_ids)

                categories = [product.category for product in products]
                category_counts = Counter(categories)

                if category_counts:
                    favorite_category = category_counts.most_common(1)[0][0]
                    favorite_categories[user_name] = favorite_category
                else:
                    favorite_categories[user_name] = None

        return favorite_categories

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

    def find_user_by_id(self, user_id):
        with Session(engine) as session:
            statement = select(User).where(User.id == user_id)
            result = session.exec(statement).first()
            return result
