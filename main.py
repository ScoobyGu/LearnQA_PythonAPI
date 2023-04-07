import requests

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

# 1. Запрос без параметра method
response = requests.get(url)
print(response.text) # Выведет "Wrong method provided"

# 2. Запрос с неправильным типом
response = requests.request("HEAD", url)
print(response.text) # Выведет "Wrong method provided"

# 3. Запрос с правильным значением method
payload = {"method": "GET"}
response = requests.get(url, params=payload)
print(response.text) # Выведет "success"

# 4. Проверка всех сочетаний
methods = ["GET", "POST", "PUT", "DELETE"]
for method in methods:
    for param_method in methods:
        if method != param_method:
            payload = {"method": param_method}
            if method == "GET":
                response = requests.get(url, params=payload)
            else:
                response = requests.post(url, data=payload)
            if response.text == "success":
                print(f"Method {method} with param method {param_method} is not detected")
        else:
            payload = {"method": param_method}
            if method == "GET":
                response = requests.get(url, params=payload)
            else:
                response = requests.post(url, data=payload)
            if response.text != "success":
                print(f"Method {method} with param method {param_method} is not detected")