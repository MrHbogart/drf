import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json={"query":1234})

print(get_response)