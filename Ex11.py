import requests

class TestHomeWorkCookie:
    def test_homework_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        print(response.cookies)
        assert "HomeWork" in response.cookies, "There is no 'HomeWork' cookie in the response"
        assert response.cookies["HomeWork"] == "hw_value", "The value of 'HomeWork' cookie is not 'hw_value'"


