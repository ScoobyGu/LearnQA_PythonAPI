import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserEdit(BaseCase):
    # Попытаемся изменить данные пользователя, будучи неавторизованными
    def test_edit_just_created_user_without_authorization(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # EDIT
        new_name = "Changed name"
        response2 = requests.put(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response2, 400)
        assert response2.content.decode("utf-8") == "Auth token not supplied", \
            f"Unexpected response content {response2.content}"

    # Попытаемся изменить данные пользователя, будучи авторизованными другим пользователем
    def test_edit_user_auth_as_another_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        old_name = register_data['username']
        user_id = self.get_json_value(response1, 'id')

        # AUTH ANOTHER USER
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, 'x-csrf-token')

        # EDIT
        new_name = "Changed Name"

        response3 = requests.put(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid},
            data={"username": new_name}
        )

        Assertions.assert_code_status(response3, 400)

        # GET
        response4 = requests.get(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid}
        )

        Assertions.assert_code_status(response4, 200)
        Assertions.assert_json_value_by_name(
            response4,
            "username",
            old_name,
            "Edit name user auth as another user"
        )

        # Попытаемся изменить email пользователя, будучи авторизованными тем же пользователем, на новый email без символа @
        def test_edit_user_with_new_wrong_email(self):
            # REGISTER
            register_data = self.prepare_registration_data()
            response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)

            Assertions.assert_code_status(response1, 200)
            Assertions.assert_json_has_key(response1, "id")

            email = register_data['email']
            password = register_data['password']
            user_id = self.get_json_value(response1, 'id')

            # LOGIN
            data = {
                'email': email,
                'password': password
            }

            response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

            auth_sid = self.get_cookie(response2, "auth_sid")
            token = self.get_header(response2, 'x-csrf-token')

            # EDIT
            new_email = 'gugmail.com'
            response3 = requests.put(
                f"https://playground.learnqa.ru/api/user/{user_id}",
                headers={'x-csrf-token': token},
                cookies={'auth_sid': auth_sid},
                data={"email": new_email}
            )

            Assertions.assert_code_status(response3, 400)

            # GET
            response4 = requests.get(
                f"https://playground.learnqa.ru/api/user/{user_id}",
                headers={'x-csrf-token': token},
                cookies={'auth_sid': auth_sid}
            )

            Assertions.assert_code_status(response4, 200)
            Assertions.assert_json_value_by_name(
                response4,
                "email",
                email,
                "Edit email address to be incorrect"
            )

    # Попытаемся изменить firstName пользователя, будучи авторизованными тем же пользователем, на очень короткое значение в один символ
    def test_edit_user_with_shot_first_name(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response1, 'id')
        first_name = register_data['firstName']

        # LOGIN
        data = {
            'email': email,
            'password': password
        }

        response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, 'x-csrf-token')

        # EDIT
        new_name = 'g'
        response3 = requests.put(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid},
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response3, 400)

        # GET
        response4 = requests.get(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid}
        )

        Assertions.assert_code_status(response4, 200)
        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            first_name,
            "Edit email address to be incorrect"
        )