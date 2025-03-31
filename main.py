
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
    logging.info(f"{user_service.paginate_and_process(5, 50) !r} ")
    logging.info(f"{product_service.paginate_and_process(10, 20) !r} ")
    logging.info(f"{basket_service.paginate_and_process(2, 25) !r} ")

    print("\n***************USERS******************\n")
    users = user_service.find_all_users()
    for user in users:
        print(user)

    print("\n***************PRODUCTS******************\n")
    products = product_service.find_all_products()
    for product in products:
        print(product)

    print("\n***************BASKETS******************\n")
    baskets = basket_service.find_all_baskets()
    for basket in baskets:
        print(basket)



if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    main()