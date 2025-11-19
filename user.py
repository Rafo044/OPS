from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str
    user_list: list

    def get_user_list(self):
        return self.user_list

    def add_user(self, user):
        self.user_list.append(user)

    def remove_user(self, user):
        self.user_list.remove(user)
