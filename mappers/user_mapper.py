from domain.dao.dao_all import User
from domain.dto.user_dto import UserDto

class UserMapper:

    def __init__(self):
        pass

    def map_user_to_entity(self, user_dto: UserDto) -> User:
        return User(
            user_dto.user_id,
            user_dto.first_name,
            user_dto.last_name,
            user_dto.latitude,
            user_dto.longitude,
            user_dto.localization,
        )