
import logging

from sqlmodel import SQLModel

from databese.database import engine
from service.basket_service import BasketService
from service.product_service import ProductService
from service.user_service import UserService


def main():
    print("Hello")
    SQLModel.metadata.create_all(engine)
    user_service = UserService()
    product_service = ProductService()
    basket_service = BasketService()
    logging.info(f"{user_service.paginate_and_process(1, 1) !r} ")
    logging.info(f"{product_service.paginate_and_process(1, 1) !r} ")
    logging.info(f"{basket_service.paginate_and_process(1, 1) !r} ")
    print(user_service.find_all_users())
    print(product_service.find_all_products())
    print(basket_service.find_all_baskets())

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    main()