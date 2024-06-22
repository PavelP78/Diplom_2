import pytest
import requests
import allure
from base.base_methods import HttpMethods
from data import MainUrl, EndPoint
from logins import UserLogin


@allure.title('Проверка создания нового пользователя')
def test_create_new_user():
    response = HttpMethods.create_new_user()
    data = response.json()
    assert response.status_code == 200
    access_token = data.get('accessToken')
    headers = {"Authorization": f"Bearer{access_token}"}
    requests.delete(f"{MainUrl.url}{EndPoint.delete_user}", headers=headers)


@allure.title('Проверка создания двух одинаковых пользователей')
def test_create_old_user():
    response = HttpMethods.create_new_user()
    data = response.json()
    response = HttpMethods.create_new_user()
    assert response.status_code == 403
    access_token = data.get('accessToken')
    headers = {"Authorization": f"Bearer{access_token}"}
    requests.delete(f"{MainUrl.url}{EndPoint.delete_user}", headers=headers)


@allure.title('Проверка создания пользователя если не заполнить одно из обязательных полей')
@pytest.mark.parametrize("user_field", [UserLogin.user_without_email, UserLogin.user_without_password,
                                        UserLogin.user_without_name])
def test_create_courier_without_field(user_field):
    response = requests.post(f"{MainUrl.url}{EndPoint.create_user}", data=user_field)
    assert response.status_code == 403
