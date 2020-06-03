import requests
url = "https://iliveinjaipo.com/"

response = requests.get(url, headers={"Accept": "application/jaipo"})

data = response.jaipo()

print(data["live"])
print(f"status: {data['status']}")