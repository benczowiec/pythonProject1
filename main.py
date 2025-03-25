
import logging

from sqlmodel import SQLModel

from databese.database import engine
from service.product_service import ProductService
from service.user_service import UserService


def main():
    print("Hello")
    SQLModel.metadata.create_all(engine)
    user_service = UserService()
    product_service = ProductService()
    logging.info(f"{user_service.paginate_and_process(1, 5) !r} ")
    logging.info(f"{product_service.paginate_and_process(10, 20) !r} ")
    print(user_service.find_all_users())
    print(product_service.find_all_products())


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    main()