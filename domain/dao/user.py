from typing import Any

from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    uuid: str
    first_name: str
    last_name: str
    latitude: str
    longitude: str
    localization: str

    def __init__(self, uuid, first_name, last_name, latitude: str, longitude: str, localization: str, **data: Any):
        super().__init__(**data)
        self.uuid = uuid
        # self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.latitude: str = latitude
        self.longitude: str = longitude
        self.localization: str = localization

    def __hash__(self):
        return hash(self.id)
