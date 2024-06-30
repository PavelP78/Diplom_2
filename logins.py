class UserLogin:

    login_create = {
        "email": "qуууiууZsz@yandex.ru",
        "password": "12211311",
        "name": "wqqLogin"
    }

    user_without_email = {
        "email": "",
        "password": "111111",
        "name": "RLogin"
    }

    user_without_password = {
        "email": "qуууiууZsz@yandex.ru",
        "password": "",
        "name": "RLogin"
    }

    user_without_name = {
        "email": "qуууiууZsz@yandex.ru",
        "password": "111111",
        "name": ""
    }


class VerificationUserLogin:

    login_user = {
        "email": "qуууiууZsz@yandex.ru",
        "password": "12211311"
    }

    incorrect_email = {
        "email": "test@yandex.ru",
        "password": "12211311"
    }

    incorrect_password = {
        "email": "qqуууiууZsz@yandex.ru",
        "password": "177777"
    }

    existent_user = {
        "email": "eq09945645cc@yandex.ru",
        "password": "114561111"
    }


class ChangeUserLogin:

    user_change_email = {
        "email": "32qwzz00zww@yandex.ru",
    }

    user_change_password = {
        "password": "111222",
    }

    user_change_name = {
        "name": "RLoginSSS"
    }
