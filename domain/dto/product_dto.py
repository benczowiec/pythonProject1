from decimal import Decimal


class ProductDto:

    def __init__(self, title: str, category: str, price: Decimal):
        self.title = title
        self.category = category
        self.price = price
