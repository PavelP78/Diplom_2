import pytest
import requests
from data import MainUrl, EndPoint
from base.base_methods import HttpMethods


@pytest.fixture
def user():
    response = HttpMethods.create_new_user()
    data = response.json()
    yield response
    access_token = data.get('accessToken')
    headers1 = {"Authorization": f"Bearer{access_token}"}
    requests.delete(f"{MainUrl.url}{EndPoint.delete_user}", headers=headers1)
