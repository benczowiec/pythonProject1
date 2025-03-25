from decimal import Decimal

from sqlmodel import SQLModel, Field


class Product(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    category: str
    price: Decimal

    def __init__(self, title: str, category: str, price: Decimal):
        self.title = title
        self.category = category
        self.price = price

    def __hash__(self):
        return hash(self.id)

