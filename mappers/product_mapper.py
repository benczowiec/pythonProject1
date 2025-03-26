from domain.dao.product import Product
from domain.dto.product_dto import ProductDto


class ProductMapper:

    def __init__(self):
        pass

    def map_product_to_entity(self, product_dto: ProductDto) -> Product:
        return Product(
            product_dto.dummy_id,
            product_dto.title,
            product_dto.price
        )