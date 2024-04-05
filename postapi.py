import requests
api_url = "https://jsonplaceholder.typicode.com/todos"
Title = input("enter your title:")
todo = {"userId": 1, "title": Title, "completed": False}
response = requests.post(url=api_url, data=todo)
response.json()
print(todo)