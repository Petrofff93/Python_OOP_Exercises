def correct_password(password):
    is_upper = False
    is_digit = False

    for pa in password:
        if pa.isupper():
            is_upper = True
        if pa.isdigit():
            is_digit = True

    return len(password) >= 8 and is_digit and is_upper


class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        if not 5 <= len(username) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = username

    def get_username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if not correct_password(password):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = password

    def get_password(self):
        return self.__password

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'


correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)

