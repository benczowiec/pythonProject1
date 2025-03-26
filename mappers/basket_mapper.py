from decimal import Decimal

from domain.dao.basket import Basket
from domain.dto.basket_dto import BasketDto
from domain.dto.product_dto import ProductDto
from mappers.product_mapper import ProductMapper


class BasketMapper:

    def __init__(self):
        self.product_mapper = ProductMapper()

    def map_dto_to_basket(self, basket_dto: BasketDto) -> Basket:
        products = [self.product_mapper.map_product_to_entity(dto) for dto in basket_dto.products]
        return Basket(total_price=basket_dto.total_price, products=products)

    def map_cart_to_basket_dto(self, basket) -> BasketDto:
        products = [
            ProductDto(
                dummy_id=product["id"],
                title=product["title"],
                price=Decimal(product["price"]),
            )
            for product in basket["products"]
        ]
        return BasketDto(total_price=Decimal(basket["total"]), products=products)