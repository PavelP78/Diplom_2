import requests
from logins import UserLogin, VerificationUserLogin
from data import MainUrl, EndPoint


class HttpMethods:

    @staticmethod
    def create_new_user():
        response = requests.post(f"{MainUrl.url}{EndPoint.create_user}", data=UserLogin.login_create)
        return response

    @staticmethod
    def verification_user():
        response = requests.post(f"{MainUrl.url}{EndPoint.verification_user}", data=VerificationUserLogin.login_user)
        return response
