import requests

print(requests.get("http://localhost:8000/items/0").json())
