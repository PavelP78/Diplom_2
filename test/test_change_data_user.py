import pytest
import requests
import allure
from data import MainUrl, EndPoint
from base.base_methods import HttpMethods
from logins import ChangeUserLogin


@allure.title('Проверка:  авторизированный пользователь может изменять email, password и name')
@pytest.mark.parametrize("change_user_field", [ChangeUserLogin.user_change_email,
                                               ChangeUserLogin.user_change_password,
                                               ChangeUserLogin.user_change_name])
def test_change_verification_data_user(change_user_field):
    response = HttpMethods.create_new_user()
    assert response.status_code == 200
    data = response.json()
    access_token = data.get('accessToken')
    headers = {"Authorization": f"Bearer{access_token}"}
    response = requests.patch(f"{MainUrl.url}{EndPoint.change_user}", headers=headers, data=change_user_field)
    assert response.status_code == 200
    requests.delete(f"{MainUrl.url}{EndPoint.delete_user}", headers=headers)


@allure.title('Проверка:  не авторизированный пользователь не может изменять email, password и name')
@pytest.mark.parametrize("change_user_field", [ChangeUserLogin.user_change_email,
                                               ChangeUserLogin.user_change_password,
                                               ChangeUserLogin.user_change_name])
def test_change_not_verification_data_user(change_user_field):
    response = HttpMethods.create_new_user()
    assert response.status_code == 200
    data = response.json()
    access_token = data.get('accessToken')
    headers = {"Authorization": f"Bearer{access_token}"}
    response = requests.patch(f"{MainUrl.url}{EndPoint.change_user}", headers=None, data=change_user_field)
    assert response.status_code == 401
    requests.delete(f"{MainUrl.url}{EndPoint.delete_user}", headers=headers)
