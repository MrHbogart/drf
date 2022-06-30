import requests


id_to_delete = 4
endpoint = f"http://localhost:8000/api/products/{id_to_delete}/"

get_response = requests.delete(endpoint)

print(get_response.status_code)