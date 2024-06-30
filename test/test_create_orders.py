import requests
import allure
from data import MainUrl, EndPoint, Ingridient


@allure.title('Проверка:  авторизированный пользователь может создать заказ')
def test_create_orders_verification_user(user):
    response, access_token, headers = user
    response = requests.post(f"{MainUrl.url}{EndPoint.create_orders}", headers=headers,
                             data=Ingridient.correct_ingridient)
    assert response.status_code == 200, "пользователь не может создать заказ"


@allure.title('Проверка:  не авторизированный пользователь  может создать заказ')
def test_create_orders_not_verification_user(user):
    response = requests.post(f"{MainUrl.url}{EndPoint.create_orders}", headers=None,
                             data=Ingridient.correct_ingridient)
    assert response.status_code == 200, "пользователь не может создать заказ"


@allure.title('Проверка:   пользователь не может создать заказ без ингридиентов')
def test_create_orders_not_verification_user(user):
    response = requests.post(f"{MainUrl.url}{EndPoint.create_orders}", headers=None, data=None)
    assert response.status_code == 400, "пользователь создал заказ без ингридиента"


@allure.title('Проверка:   пользователь не может создать заказ с неверным хешем ингридиентов')
def test_create_orders_not_verification_user(user):
    response = requests.post(f"{MainUrl.url}{EndPoint.create_orders}", headers=None,
                             data=Ingridient.not_correct_ingridient)
    assert response.status_code == 500, "пользователь создал заказ"
