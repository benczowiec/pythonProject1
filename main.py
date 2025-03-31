import csv
import logging
from typing import List, Dict

from sqlmodel import SQLModel, Session, select

from databese.database import engine
from domain.dao.dao_all import Basket
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
    for user in user_service.find_all_users():
        print(user)

    print("\n***************PRODUCTS******************\n")
    for product in product_service.find_all_products():
        print(product)

    print("\n***************BASKETS******************\n")
    for basket in basket_service.find_all_baskets():
        print(basket)

    print("\n***************Categories******************\n")
    favorite_categories = user_service.find_favorite_categories_for_users()
    for user_name, category in favorite_categories.items():
        print(f"Ulubiona kategoria zamawiana przez użytkownika {user_name} to: {category}")

    with open('favorite_categories.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["User Name", "Favorite Category"])
        for user_name, category in favorite_categories.items():
            writer.writerow([user_name, category])

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    main()



