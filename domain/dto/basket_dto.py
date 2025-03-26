from decimal import Decimal

from domain.dto.product_dto import ProductDto


class BasketDto:

    def __init__(self, total_price: Decimal, products: list[ProductDto]):
        self.total_price = total_price
        self.products = products