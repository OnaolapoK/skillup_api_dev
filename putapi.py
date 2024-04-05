import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
response.json()
Title = input("enter your title:")
todo = {"userId": 2, "title": Title, "completed": True}
response = requests.put(api_url, json=todo)
print(response.json())
print(response.status_code)