import json

json_text = '{"messages": [{"message": "Hello World!"}, {"message": "Привет Мир!"}]}'
data = json.loads(json_text)
print(data['messages'][1]['message'])

