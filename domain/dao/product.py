from decimal import Decimal
from typing import Optional, Any

from sqlmodel import SQLModel, Field, Relationship

from domain.dao.basket import Basket


class Product(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    dummy_id: int
    title: str
    price: Decimal
    basket_id: Optional[int] = Field(default=None, foreign_key="basket.id")
    basket: Optional["Basket"] = Relationship(back_populates="products")

    def __init__(self, dummy_id: int, title: str, price: Decimal, **data: Any):
        super().__init__(**data)
        self.dummy_id = dummy_id
        self.title = title
        self.price = price

    def __hash__(self):
        return hash(self.dummy_id)

