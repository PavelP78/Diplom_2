class MainUrl:
    url = 'https://stellarburgers.nomoreparties.site'


class EndPoint:
    create_user = "/api/auth/register"
    verification_user = "/api/auth/login"
    regestration_user = "/api/auth/register"
    change_user = "/api/auth/user"
    delete_user = "/api/auth/user"
    create_orders = "/api/orders"
    get_orders = "/api/orders"
    headers = {"Content-Type": "application/json"}


class Ingridient:
    correct_ingridient = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "609646e4dc916e00276b2870"]}

    not_correct_ingridient = {
        "ingredients": ["60d3b41acab0026a733c6", "609646e4dc91276b2870"]}
