import requests
url = "https://iliveinjaipo.com/search"

response = requests.get(
	url,
	headers={"Accept": "application/jaipo"},
	params={"term": "cat", "limit": 1}
)

data = response.json()
print(data["results"])