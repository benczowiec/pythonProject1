from decimal import Decimal


class ProductDto:

    def __init__(self, product_id: int, title: str, category: str, price: Decimal):
        self.product_id = product_id
        self.title = title
        self.category = category
        self.price = price