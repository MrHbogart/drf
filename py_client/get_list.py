import requests

endpoint = "http://localhost:8000/api/mixin/"

get_response = requests.get(endpoint)

json = get_response.json()

for i in json:
    print(i)