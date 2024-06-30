from faker import Faker
import os


def sign_up_data(self):
    file_path = os.path.dirname(__file__)
    fake = Faker()
    self.MY_LOGIN = fake.email()
    self.MY_PASSWORD = fake.password()
    self.MY_NAME = fake.name()
    user_data = {"email": self.MY_LOGIN, "password": self.MY_PASSWORD, "name": self.MY_NAME}
    with open(os.path.join(file_path, 'temp_data_login.py'), 'w') as file:
        file.write(f"MY_LOGIN = '{self.MY_LOGIN}'\n")
    with open(os.path.join(file_path, 'temp_data_password.py'), 'w') as file:
        file.write(f"MY_PASSWORD = '{self.MY_PASSWORD}'\n")
    with open(os.path.join(file_path, 'temp_data_name.py'), 'w') as file:
        file.write(f"MY_NAME = '{self.MY_NAME}'\n")
    return user_data
