import requests

endpoint = "http://localhost:8000/api/create/"

data = {"title":"asdfg",
        "content":"wertyuiopsdfghjk",
        "price":123.90}
get_response = requests.post(endpoint, json=data)

print(get_response.status_code)