import uuid

import reverse_geocode


class User:

    def __init__(self, id, first_name, last_name, latitude: str, longitude: str):
        self.uuid = uuid.uuid4()
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self.latitude: str = latitude
        self.longitude: str = longitude
        self.localization: str = ""

    def find_localization(self):
        location = reverse_geocode.get((self.latitude, self.longitude))
        print(location)
        self.localization = location["country"]

    def __str__(self):
        return f"User with ID: {self._id} -> {self._first_name} {self._last_name} {self.latitude} {self.longitude}\n"

    def __repr__(self):
        return f"User with ID: {self._id} -> {self._first_name} {self._last_name} \n"