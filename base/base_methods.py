import requests
from logins import UserLogin, VerificationUserLogin
from data import MainUrl, EndPoint
from helper import sign_up_data
import temp_data_name
import temp_data_login
import temp_data_password
import temp_data


class StellarBurgersAPI:
    def __init__(self):
        self.MY_LOGIN = None
        self.MY_PASSWORD = None
        self.MY_NAME = None

    @property
    def sign_up_data(self):
        return sign_up_data(self)

    @staticmethod
    def create_new_user(sign_up_data):
        new_user_response = requests.post(f"{MainUrl.url}{EndPoint.registration_user}", data=sign_up_data)
        return new_user_response

    def get_login(self):
        return self.MY_LOGIN

    def get_password(self):
        return self.MY_PASSWORD

    @staticmethod
    def verification_user(user_data):
        response = requests.post(f"{MainUrl.url}{EndPoint.verification_user}",
                                 data=user_data)
        return response

    @staticmethod
    def get_access_token(new_user_response):
        access_token = new_user_response.json().get("accessToken")
        return access_token

    @staticmethod
    def delete_user(access_token):
        headers = {"Authorization": f"Bearer{access_token}"}
        response = requests.delete(f"{MainUrl.url}{EndPoint.delete_user}", headers=headers)
        return response


class HttpMethods:

    @staticmethod
    def create_new_user():
        response = requests.post(f"{MainUrl.url}{EndPoint.create_user}", data=UserLogin.login_create)
        return response

    @staticmethod
    def verification_user():
        response = requests.post(f"{MainUrl.url}{EndPoint.verification_user}", data=VerificationUserLogin.login_user)
        return response

    @staticmethod
    def create_faker_user():
        special_user_data = {
            "email": temp_data_login.MY_LOGIN,
            "password": temp_data_password.MY_PASSWORD,
            "name": temp_data_name.MY_NAME
        }
        special_user_response = requests.post(f"{MainUrl.url}{EndPoint.registration_user}", data=special_user_data)
        return special_user_response

    @staticmethod
    def verification_faker_user():
        data = {
            "email": temp_data_login.MY_LOGIN,
            "password": temp_data_password.MY_PASSWORD,
        }
        response = requests.post(f"{MainUrl.url}{EndPoint.verification_user}",
                                 data=data)
        return response

    @staticmethod
    def delete_user():
        headers = {"Authorization": f"Bearer{temp_data.access_token}"}
        response = requests.delete(f"{MainUrl.url}{EndPoint.delete_user}", headers=headers)
        return response
