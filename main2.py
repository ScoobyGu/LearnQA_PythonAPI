import requests
import time

# создаем задачу
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
parsed_response = response.json()
token = parsed_response["token"]
seconds_to_wait = parsed_response["seconds"]

print(f"Task created with token: {token} and {seconds_to_wait} seconds to wait")

# делаем запрос с токеном до того, как задача готова
response = requests.get(f"https://playground.learnqa.ru/ajax/api/longtime_job?token={token}")
parsed_response = response.json()
status = parsed_response["status"]
print(f"Status of the task before waiting: {status}")

# ждем нужное количество секунд
time.sleep(seconds_to_wait)

# делаем запрос с токеном после того, как задача готова
response = requests.get(f"https://playground.learnqa.ru/ajax/api/longtime_job?token={token}")
parsed_response = response.json()
status = parsed_response["status"]
if status == "Job is NOT ready":
    print("Error: job is not ready")
elif status == "Job is ready":
    result = parsed_response["result"]
    print(f"Result of the task: {result}")
else:
    print("Error: unknown status")
