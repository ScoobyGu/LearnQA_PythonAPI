import requests

class TestHeader:
    def test_header(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        headers = response.headers
        print(headers)
        assert "x-secret-homework-header" in response.headers, "There is no 'x-secret-homework-header' cookie in the response"
        assert response.headers.get("x-secret-homework-header") == 'Some secret value'





