from decimal import Decimal
from typing import Any, List, TYPE_CHECKING, Optional

from sqlmodel import SQLModel, Field, Relationship


class Product(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    product_id: int
    title: str
    category: str
    price: Decimal
    baskets: List['Basket'] = Relationship(back_populates="product")

    def __init__(self, product_id: int, title: str, category: str, price: Decimal, **data: Any):
        super().__init__(**data)
        self.product_id = product_id
        self.title = title
        self.category = category
        self.price = price

    def __hash__(self):
        return hash(self.product_id)


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int
    first_name: str
    last_name: str
    latitude: str
    longitude: str
    localization: str
    baskets: List["Basket"] = Relationship(back_populates="user")

    def __init__(self, user_id, first_name, last_name, latitude: str, longitude: str, localization: str, **data: Any):
        super().__init__(**data)
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.latitude: str = latitude
        self.longitude: str = longitude
        self.localization: str = localization

    def __hash__(self):
        return hash(self.user_id)

class Basket(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    basket_id: int
    total_price: Decimal
    quantity: int
    user_id: Optional[int] = Field(foreign_key="user.user_id")
    product_id: Optional[int] = Field(foreign_key="product.product_id")
    user: Optional['User'] = Relationship(back_populates="baskets")
    product: Optional['Product'] = Relationship(back_populates="baskets")

    def __init__(self, basket_id, total_price: Decimal, quantity, user, product, **data: Any):
        super().__init__(**data)
        self.basket_id = basket_id
        self.total_price = total_price
        self.quantity = quantity
        self.user = user
        self.product = product

    def __hash__(self):
        return hash(self.id)