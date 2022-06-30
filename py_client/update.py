import requests

id_to_update = 2

endpoint = f"http://localhost:8000/api/products/{id_to_update}/"

data = {"title":"2222",
        "content":"bukmk",
        "price":321.90}


get_response = requests.put(endpoint, json=data)

print(get_response.status_code)