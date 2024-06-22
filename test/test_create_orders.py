import requests
import allure
from data import MainUrl, EndPoint, Ingridient
from base.base_methods import HttpMethods


@allure.title('Проверка:  авторизированный пользователь может создать заказ')
def test_create_orders_verification_user():
    response = HttpMethods.create_new_user()
    assert response.status_code == 200
    data = response.json()
    access_token = data.get('accessToken')
    headers = {"Authorization": f"Bearer{access_token}"}
    response = requests.post(f"{MainUrl.url}{EndPoint.create_orders}", headers=headers,
                             data=Ingridient.correct_ingridient)
    assert response.status_code == 200
    requests.delete(f"{MainUrl.url}{EndPoint.delete_user}", headers=headers)


@allure.title('Проверка:  не авторизированный пользователь  может создать заказ')
def test_create_orders_not_verification_user():
    response = HttpMethods.create_new_user()
    assert response.status_code == 200
    data = response.json()
    access_token = data.get('accessToken')
    headers = {"Authorization": f"Bearer{access_token}"}
    response = requests.post(f"{MainUrl.url}{EndPoint.create_orders}", headers=None,
                             data=Ingridient.correct_ingridient)
    assert response.status_code == 200
    requests.delete(f"{MainUrl.url}{EndPoint.delete_user}", headers=headers)


@allure.title('Проверка:   пользователь не может создать заказ без ингридиентов')
def test_create_orders_not_verification_user():
    response = HttpMethods.create_new_user()
    assert response.status_code == 200
    data = response.json()
    access_token = data.get('accessToken')
    headers = {"Authorization": f"Bearer{access_token}"}
    response = requests.post(f"{MainUrl.url}{EndPoint.create_orders}", headers=None, data=None)
    assert response.status_code == 400
    requests.delete(f"{MainUrl.url}{EndPoint.delete_user}", headers=headers)


@allure.title('Проверка:   пользователь не может создать заказ с неверным хешем ингридиентов')
def test_create_orders_not_verification_user():
    response = HttpMethods.create_new_user()
    assert response.status_code == 200
    data = response.json()
    access_token = data.get('accessToken')
    headers = {"Authorization": f"Bearer{access_token}"}
    response = requests.post(f"{MainUrl.url}{EndPoint.create_orders}", headers=None,
                             data=Ingridient.not_correct_ingridient)
    assert response.status_code == 500
    requests.delete(f"{MainUrl.url}{EndPoint.delete_user}", headers=headers)
