from decimal import Decimal
from typing import List, Any

from sqlmodel import SQLModel, Field, Relationship



class Basket(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    products: List["Product"] = Relationship(back_populates="basket")
    total_price: Decimal

    def __init__(self, total_price: Decimal, products, **data: Any):
        super().__init__(**data)
        self.total_price = total_price
        self.products = products

    def __hash__(self):
        return hash(self.id)

