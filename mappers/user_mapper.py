from domain.dao.user import User
from domain.dto.user_dto import UserDto

class UserMapper:

    def __init__(self):
        pass

    def map_user_to_entity(self, user_dto: UserDto) -> User:
        return User(
            str(user_dto.uuid),
            user_dto.first_name,
            user_dto.last_name,
            user_dto.latitude,
            user_dto.longitude,
            user_dto.localization,
        )