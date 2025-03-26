from decimal import Decimal
from typing import Set

from sqlmodel import Session, select

from controller.dummy_connector import DummyConnector
from databese.database import engine
from domain.dao.basket import Basket
from domain.dao.product import Product
from domain.dto.basket_dto import BasketDto
from domain.dto.product_dto import ProductDto
from mappers.basket_mapper import BasketMapper


class BasketService:
    basket_endpoint = "carts"

    def __init__(self):
        self.basket_controller = DummyConnector()
        self.basket_mapper = BasketMapper()

    def process_baskets(self, baskets):
        processed_baskets: Set[Basket] = set()
        for basket in baskets:
            new_basket: BasketDto = self.basket_mapper.map_cart_to_basket_dto(basket)
            processed_baskets.add(self.basket_mapper.map_dto_to_basket(new_basket))
        print(len(processed_baskets))
        self.save_baskets(processed_baskets)

    def paginate_and_process(self, num_pages, limit):
        skip = 0
        for i in range(num_pages):
            data = self.basket_controller.get_data(skip, limit, self.basket_endpoint)
            self.process_baskets(data["carts"])
            skip += limit

    def save_baskets(self, baskets: set[Basket]):
        with Session(engine) as session:
            session.add_all(baskets)
            session.commit()

    def find_all_baskets(self):
        with Session(engine) as session:
            statement = select(Basket)
            results = session.exec(statement)
            return results.all()
