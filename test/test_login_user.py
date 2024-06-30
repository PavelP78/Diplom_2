import pytest
import requests
import allure
from data import MainUrl, EndPoint
from base.base_methods import HttpMethods
from logins import VerificationUserLogin


@allure.title('Проверка:  авторизация существующего пользователя')
def test_verification_user(user):
    response = HttpMethods.verification_user()
    assert response.status_code == 200, "пользователь не авторизирован"


@allure.title('Проверка:  авторизация  пользователя с неверным логином и паролем')
@pytest.mark.parametrize("verification_field", [VerificationUserLogin.incorrect_email,
                                                VerificationUserLogin.incorrect_password])
def test_verification_with_error_field(verification_field):
    response = requests.post(f"{MainUrl.url}{EndPoint.verification_user}", data=verification_field)
    assert response.status_code == 401, "пользователь  авторизирован"
