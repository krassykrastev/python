from project.user import User
from project.library import Library


class Registration:
    @staticmethod
    def add_user(user: User, library: Library):
        for u in library.user_records:
            if u.user_id == user.user_id:
                return f"User with id = {u.user_id} already registered in the library!"
        library.user_records.append(user)

    @staticmethod
    def remove_user(user: User, library: Library):
        for u in library.user_records:
            if u.user_id == user.user_id:
                library.user_records.remove(u)
                return
        return "We could not find such user to remove!"

    @staticmethod
    def change_username(user_id: int, new_username: str, library: Library):
        for u in library.user_records:
            if u.user_id == user_id:
                if u.username == new_username:
                    return "Please check again the provided username - it should be different than the username used so far!"
                u.username = new_username
                return f"Username successfully changed to: {new_username} for user id: {user_id}"
        return f"There is no user with id = {user_id}!"
    