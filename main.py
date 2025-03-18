
import logging
from service.user_service import UserService


def main():
    print("Hello")
    user_service = UserService()

    #user_service.fetch_all_user()
    #user_service.fetch_all_users_info(10)
    logging.info(f"{user_service.paginate_and_process(2, 5) !r} ")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    main()