import requests

id_to_get = 3
endpoint = f"http://localhost:8000/api/products/{id_to_get}/"

get_response = requests.get(endpoint)

print(get_response.status_code)
print(get_response.json())