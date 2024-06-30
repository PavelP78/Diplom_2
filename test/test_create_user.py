import pytest
import requests
import allure
from base.base_methods import HttpMethods
from data import MainUrl, EndPoint
from logins import UserLogin


@allure.title('Проверка создания нового пользователя')
def test_create_faker_new_user(enter_and_delete_user):
    pass


@allure.title('Проверка создания нового пользователя')
def test_create_new_user(user):
    pass


@allure.title('Проверка создания двух одинаковых пользователей')
def test_create_old_user(user):
    response = HttpMethods.create_new_user()
    assert response.status_code == 403, "Двух одинаковых пользователей можно создать"


@allure.title('Проверка создания двух одинаковых пользователей')
def test_create_two_identical_users(create_faker_user):
    response = HttpMethods.create_faker_user()
    assert response.status_code == 403, "Двух одинаковых пользователей можно создать"
    response = HttpMethods.delete_user()
    assert response.status_code == 202, "Пользователь не удален"


@allure.title('Проверка создания пользователя если не заполнить одно из обязательных полей')
@pytest.mark.parametrize("user_field", [UserLogin.user_without_email, UserLogin.user_without_password,
                                        UserLogin.user_without_name])
def test_create_courier_without_field(user_field):
    response = requests.post(f"{MainUrl.url}{EndPoint.create_user}", data=user_field)
    assert response.status_code == 403, "Пользователь создан"
