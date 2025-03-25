from typing import Set

from sqlmodel import Session, select

from controller.dummy_connector import DummyConnector
from databese.database import engine
from domain.dao.product import Product
from domain.dto.product_dto import ProductDto
from mappers.product_mapper import ProductMapper


class ProductService:
    product_endpoint = "products"

    def __init__(self):
        self.product_controller = DummyConnector()
        self.product_mapper = ProductMapper()

    def process_products(self, products):
        processed_products: Set[Product] = set()
        for product in products:
            new_product: ProductDto = ProductDto(product["title"], product["category"], product["price"])
            processed_products.add(self.product_mapper.map_product_to_entity(new_product))
        self.save_products(processed_products)

    def paginate_and_process(self, num_pages, limit):
        skip = 0
        for i in range(num_pages):
            data = self.product_controller.get_data(skip, limit, self.product_endpoint)
            self.process_products(data["products"])
            skip += limit

    def save_products(self, products: set[Product]):
        with Session(engine) as session:
            session.add_all(products)
            session.commit()

    def find_all_products(self):
        with Session(engine) as session:
            statement = select(Product)
            results = session.exec(statement)
            return results.all()