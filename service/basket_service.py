from typing import Set, List

from sqlmodel import Session, select

from controller.dummy_connector import DummyConnector
from databese.database import engine
from domain.dao.dao_all import Basket
from domain.dto.basket_dto import BasketDto
from service.product_service import ProductService
from service.user_service import UserService


class BasketService:
    basket_endpoint = "carts"

    def __init__(self):
        self.basket_controller = DummyConnector()
        self.product_service = ProductService()
        self.user_service = UserService()

    def process_baskets(self, baskets):
        processed_baskets: Set[Basket] = set()
        for basket in baskets:
            user_id = basket["userId"]
            total_price = basket["total"]
            basket_id = basket["id"]
            new_baskets: List[BasketDto] = [
                BasketDto(basket_id, total_price, product["quantity"], user_id, product["id"])
                for product in basket["products"]
            ]

            product_ids = [basket.product_id for basket in new_baskets]

            products = self.product_service.find_all_products_by(product_ids)
            user = self.user_service.find_user_by_id(user_id)

            for basket_dto in new_baskets:
                product = next((p for p in products if p.product_id == basket_dto.product_id), None)
                if product:
                    processed_baskets.add(Basket(
                        basket_id=basket_dto.basket_id,
                        total_price=total_price,
                        quantity=basket_dto.quantity,
                        user=user,
                        product=product
                    ))
        print(len(processed_baskets))
        self.save_baskets(processed_baskets)

    def paginate_and_process(self, num_pages, limit):
        skip = 0
        for i in range(num_pages):
            data = self.basket_controller.get_data(skip, limit, self.basket_endpoint)
            self.process_baskets(data["carts"])
            skip += limit

    # def save_baskets(self, baskets: set[Basket]):
    #     with Session(engine) as session:
    #         session.add_all(baskets)
    #         session.commit()

    def save_baskets(self, baskets):
        with Session(engine) as session:
            for basket in baskets:
                session.merge(basket)  # Use merge instead of add
            session.commit()

    def find_all_baskets(self):
        with Session(engine) as session:
            statement = select(Basket)
            results = session.exec(statement)
            return results.all()
