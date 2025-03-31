from domain.dao.dao_all import Product
from domain.dto.product_dto import ProductDto


class ProductMapper:

    def __init__(self):
        pass

    def map_product_to_entity(self, product_dto: ProductDto) -> Product:
        return Product(
            product_dto.product_id,
            product_dto.title,
            product_dto.category,
            product_dto.price
        )