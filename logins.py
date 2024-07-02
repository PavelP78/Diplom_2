class UserLogin:

    login_create = {
        "email": "e45wrtzsa@yandex.com",
        "password": "12211311",
        "name": "wqqLogin"
    }

    user_without_email = {
        "email": "",
        "password": "111111",
        "name": "RLogin"
    }

    user_without_password = {
        "email": "e45wrtzsa@yandex.com",
        "password": "",
        "name": "RLogin"
    }

    user_without_name = {
        "email": "e45wrtzsa@yandex.com",
        "password": "111111",
        "name": ""
    }


class VerificationUserLogin:

    login_user = {
        "email": "e45wrtzsa@yandex.com",
        "password": "12211311"
    }

    incorrect_email = {
        "email": "test@yandex.ru",
        "password": "12211311"
    }

    incorrect_password = {
        "email": "e45wrtzsa@yandex.com",
        "password": "177777"
    }

    existent_user = {
        "email": "eq09945645cc@yandex.ru",
        "password": "114561111"
    }


class ChangeUserLogin:

    user_change_email = {
        "email": "3eeeee0zww@yandex.ru",
    }

    user_change_password = {
        "password": "111222",
    }

    user_change_name = {
        "name": "RLoginSSS"
    }
