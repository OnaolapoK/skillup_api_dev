import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"
Title = input("enter your title:")
todo = {"title": Title}
response = requests.patch(api_url, json=todo)
response.json()
