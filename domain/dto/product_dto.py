from decimal import Decimal


class ProductDto:

    def __init__(self, dummy_id: int, title: str, price: Decimal):
        self.dummy_id = dummy_id
        self.title = title
        self.price = price
