import requests
import allure
from data import MainUrl, EndPoint
from base.base_methods import HttpMethods


@allure.title('Проверка:  авторизированный пользователь может получить заказ')
def test_get_orders_verification_user():
    response = HttpMethods.create_new_user()
    assert response.status_code == 200
    data = response.json()
    access_token = data.get('accessToken')
    headers = {"Authorization": f"Bearer{access_token}"}
    response = requests.get(f"{MainUrl.url}{EndPoint.get_orders}", headers=headers)
    assert response.status_code == 200
    requests.delete(f"{MainUrl.url}{EndPoint.delete_user}", headers=headers)


@allure.title('Проверка:  не авторизированный пользователь не может получить заказ')
def test_get_orders_not_verification_user():
    response = HttpMethods.create_new_user()
    assert response.status_code == 200
    data = response.json()
    access_token = data.get('accessToken')
    headers = {"Authorization": f"Bearer{access_token}"}
    response = requests.get(f"{MainUrl.url}{EndPoint.get_orders}", headers=None)
    assert response.status_code == 401
    requests.delete(f"{MainUrl.url}{EndPoint.delete_user}", headers=headers)
