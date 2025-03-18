import reverse_geocode
from geopy.exc import GeocoderServiceError

from controller.dummy_connector import DummyConnector
from models.user import User


class UserService:
    def __init__(self):
        self.user_controller = DummyConnector()

    def process_users(self, users):
        for user in users:
            new_user: User = User(user["id"], user["firstName"], user["lastName"],
                                  user["address"]["coordinates"]["lat"],
                                  user["address"]["coordinates"]["lng"])
            new_user.find_localization()

    def paginate_and_process(self, num_pages, limit):
        skip = 0
        for i in range(num_pages):
            data = self.user_controller.get_user_info(skip, limit)
            self.process_users(data["users"])
            skip += limit
