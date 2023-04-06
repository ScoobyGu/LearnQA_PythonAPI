import requests

url = "https://playground.learnqa.ru/api/long_redirect"
response = requests.get(url)

redirect_count = len(response.history)
final_url = response.url

print("Количество редиректов: ", redirect_count)
print("Итоговый URL: ", final_url)


