import re


#  1


class Email:

    def __init__(self):
        self._email = None

    def __str__(self):
        if self._email is not None:
            return self._email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email_str: str):
        if self._validate(email_str):
            self._email = email_str

    def _validate(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not email.isdigit():
            if re.fullmatch(regex, email):
                return email
            else:
                raise TypeError("Invalid Email")


if __name__ == "__main__":
    email_instance = Email()
    email_instance.email = "hello@email.com"
    print(email_instance)
