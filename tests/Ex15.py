import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime
import pytest

class TestUserRegister(BaseCase):
    def setup_method(self):
        base_part = "learnqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"{base_part}{random_part}@{domain}"

    def test_create_user_successfully(self):
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.email
            }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

# Тест на создание пользователя с некорректным email - без символа @
    def test_create_user_with_incorrect_email(self):
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': 'gu.gmail.com'
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        assert response.content.decode('utf-8') == 'Invalid email format', 'User create with wrong email'

# Тест на создание пользователя без указания одного из полей
    params = [
        ({'username': 'learnqa', 'firstName': 'learnqa', 'lastName': 'learnqa', 'email': 'gu@gmail.com'},
         'password'),
        (
        {'password': '123', 'firstName': 'learnqa', 'lastName': 'learnqa', 'email': 'gu@gmail.com'}, 'username'),
        (
        {'password': '123', 'username': 'learnqa', 'lastName': 'learnqa', 'email': 'gu@gmail.com'}, 'firstName'),
        (
        {'password': '123', 'username': 'learnqa', 'firstName': 'learnqa', 'email': 'gu@gmail.com'}, 'lastName'),
        ({'password': '123', 'username': 'learnqa', 'firstName': 'learnqa', 'lastName': 'learnqa'}, 'email')
    ]

    @pytest.mark.parametrize('param', params)
    def test_create_user_without_parameter(self, param):
        data, missing_parameter = param

        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode('utf-8') == f"The following required params are missed: {missing_parameter}"

# Тест на создание пользователя с очень коротким именем в один символ
    def test_create_user_with_shot_first_name(self):
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'l',
            'lastName': 'learnqa',
            'email': 'gu@gmail.com'
        }

        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode('utf-8') == "The value of 'firstName' field is too short", 'User create with shot firstName'


# Тест на создание пользователя с очень длинным именем - длиннее 250 символов
    def test_create_user_with_long_first_name(self):
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': '55fhhyrylnhytnfhhgrhjhytelnhyrhtkrlshtrwhyjytwjkbjhkvkvgbjkjbvligtrwhyhytjhytejnytejnytednyhtdgntdgvfeabtabhtgabsnbtgrfntgrfsntgrfsntgrfsntgrsfntgrsntrsntrsntrsntrsntgrsntgrsntgsntgrsfntgfsnbgfngfnyhnmgbrghtrsnjhynyfsngtfstsrhtrsnjnyutdngfsbfedaeawerg',
            'lastName': 'learnqa',
            'email': 'gu@gmail.com'
        }

        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode('utf-8') == "The value of 'firstName' field is too long", 'User create with long firstName'



