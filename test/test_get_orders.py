import requests
import allure
from data import MainUrl, EndPoint
from temp_data import access_token


@allure.title('Проверка:  авторизированный пользователь может получить заказ')
def test_get_orders_verification_user(user):
    response, access_token, headers = user
    order_response = requests.get(f"{MainUrl.URL}{EndPoint.get_orders}", headers=headers)
    assert order_response.status_code == 200, "авторизированный пользователь не может получить заказ"


@allure.title('Проверка:  не авторизированный пользователь не может получить заказ')
def test_get_orders_not_verification_user(user):
    headers = {"Authorization": f"Bearer{access_token}"}
    response = requests.get(f"{MainUrl.URL}{EndPoint.get_orders}", headers=None)
    assert response.status_code == 401, "авторизированный пользователь  может получить заказ"
