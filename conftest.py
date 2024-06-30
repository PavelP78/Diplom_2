import pytest
from base.base_methods import StellarBurgersAPI
import json
import os
from base.base_methods import HttpMethods
from data import MainUrl, EndPoint
import requests


def write_to_file(access_token):
    file_path = os.path.join(os.path.dirname(__file__), 'temp_data.py')
    token_data = {'access_token': access_token}
    token_data_json = json.dumps(token_data['access_token'])
    formatted_line = "access_token = " + token_data_json.replace('"', "'") + "\n"
    with open(file_path, 'w') as file:
        file.write(formatted_line)


@pytest.fixture
def create_faker_user():
    stellar_burgers_api = StellarBurgersAPI()
    sign_up_data = stellar_burgers_api.sign_up_data
    new_user_response = stellar_burgers_api.create_new_user(sign_up_data)
    access_token = stellar_burgers_api.get_access_token(new_user_response)
    write_to_file(access_token)
    assert new_user_response.status_code == 200, "Новый пользователь не создан"
    yield access_token


@pytest.fixture
def delete_faker_user(create_faker_user):
    stellar_burgers_api = StellarBurgersAPI()
    access_token = create_faker_user
    response = stellar_burgers_api.delete_user(access_token)
    assert response.status_code == 202, "Пользователь не удален"


@pytest.fixture
def enter_and_delete_user():
    stellar_burgers_api = StellarBurgersAPI()
    sign_up_data = stellar_burgers_api.sign_up_data
    new_user_response = stellar_burgers_api.create_new_user(sign_up_data)
    access_token = stellar_burgers_api.get_access_token(new_user_response)
    write_to_file(access_token)
    assert new_user_response.status_code == 200, "Новый пользователь не создан"
    yield access_token
    response = stellar_burgers_api.delete_user(access_token)
    assert response.status_code == 202, "Пользователь не удален"


@pytest.fixture
def user():
    response = HttpMethods.create_new_user()
    assert response.status_code == 200, "Новый пользователь не создан"
    data = response.json()
    access_token = data.get('accessToken')
    headers = {"Authorization": f"Bearer{access_token}"}
    yield response, access_token, headers
    response = requests.delete(f"{MainUrl.url}{EndPoint.delete_user}", headers=headers)
    assert response.status_code == 202, "Пользователь не удален"
