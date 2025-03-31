# from decimal import Decimal
# from typing import Any, Optional, TYPE_CHECKING
#
# from sqlmodel import SQLModel, Field, Relationship
#
# from domain.dao.product import Product
# from domain.dao.user import User
#
# if TYPE_CHECKING:
#     from domain.dao.product import Product
#     from domain.dao.user import User
#
# class Basket(SQLModel, table=True):
#     id: int = Field(default=None, primary_key=True)
#     basket_id: int
#     total_price: Decimal
#     quantity: int
#     user_id: Optional[int] = Field(foreign_key="user.user_id")
#     product_id: Optional[int] = Field(foreign_key="product.product_id")
#     user: Optional['User'] = Relationship(back_populates="baskets")
#     product: Optional['Product'] = Relationship(back_populates="baskets")
#
#     def __init__(self, basket_id, total_price: Decimal, quantity, user, product, **data: Any):
#         super().__init__(**data)
#         self.basket_id = basket_id
#         self.total_price = total_price
#         self.quantity = quantity
#         self.user = user
#         self.product = product
#
#     def __hash__(self):
#         return hash(self.id)
