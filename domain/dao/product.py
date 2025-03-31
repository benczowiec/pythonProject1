# from decimal import Decimal
# from typing import Any, List, TYPE_CHECKING
#
# from sqlmodel import SQLModel, Field, Relationship
#
# from domain.dao.basket import Basket
#
# if TYPE_CHECKING:
#     from domain.dao.basket import Basket
#
# class Product(SQLModel, table=True):
#     id: int = Field(default=None, primary_key=True)
#     product_id: int
#     title: str
#     category: str
#     price: Decimal
#     baskets: List['Basket'] = Relationship(back_populates="product")
#
#     def __init__(self, product_id: int, title: str, category: str, price: Decimal, **data: Any):
#         super().__init__(**data)
#         self.product_id = product_id
#         self.title = title
#         self.category = category
#         self.price = price
#
#     def __hash__(self):
#         return hash(self.product_id)
