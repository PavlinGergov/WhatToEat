import re

class Validation:

    def __init__(self):
        pass

    def check_validation(self, username, email, password):
        return self.__check_username(username) \
        and self.__check_email(email) \
        and self.__check_password(password)

    def __check_username(self, username):
        return len(username) > 4
           
    def __check_email(self, email):
        return re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email)

    def __check_password(self, password):
        return re.search(r'\d', password) and len(password) > 4
