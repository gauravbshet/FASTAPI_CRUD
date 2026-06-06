from models import user_models
from schemas import user_schemas


class UserRepository:
    def __init__(self):
        self.users = []

    def add_user(self, user: User):
        self.users.append(user)

    def get_user(self, user_id: int) -> User:
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def update_user(self, id: int, name: str, email: str) -> User:
        user = self.get_user(id)
        if user:
            user.name = name
            user.email = email
            return user
        return None

    def delete_user(self, user_id: int):
        for user in self.users:
            if user.id == user_id:
                self.users.remove(user)
                return True
        return False
