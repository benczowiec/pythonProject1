from uuid import uuid4

import reverse_geocode


class UserDto:

    def __init__(self, first_name, last_name, latitude: str, longitude: str):
        self.uuid = uuid4()
        self.first_name = first_name
        self.last_name = last_name
        self.latitude: str = latitude
        self.longitude: str = longitude
        self.localization: str = ""

    def find_localization(self):
        location = reverse_geocode.get((self.latitude, self.longitude))
        print(location)
        self.localization = location["country"]

    def __str__(self):
        return f"User with ID: -> {self.first_name} {self.last_name} {self.latitude} {self.longitude}\n"

    def __repr__(self):
        return f"User with ID: -> {self.first_name} {self.last_name} \n"

    def __hash__(self):
        return hash(self.uuid)

    # @property
    # def last_name(self):
    #     return self.last_name
    #
    # @property
    # def first_name(self):
    #     return self.first_name
    #
    # @property
    # def id(self):
    #     return self._id
