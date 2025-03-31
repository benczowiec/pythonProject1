# from typing import Any, List
#
# from sqlmodel import SQLModel, Field, Relationship
#
# from domain.dao.basket import Basket
#
#
# class User(SQLModel, table=True):
#     id: int = Field(default=None, primary_key=True)
#     user_id: int
#     first_name: str
#     last_name: str
#     latitude: str
#     longitude: str
#     localization: str
#     baskets: List["Basket"] = Relationship(back_populates="user")
#
#     def __init__(self, user_id, first_name, last_name, latitude: str, longitude: str, localization: str, **data: Any):
#         super().__init__(**data)
#         self.user_id = user_id
#         self.first_name = first_name
#         self.last_name = last_name
#         self.latitude: str = latitude
#         self.longitude: str = longitude
#         self.localization: str = localization
#
#     def __hash__(self):
#         return hash(self.user_id)
