import json
import urllib.request

URL = "https://jsonplaceholder.typicode.com/users/1"

req = urllib.request.Request(URL, headers={"Accept": "application/json"})
with urllib.request.urlopen(req, timeout=10) as resp:
    print("Статус:", resp.status)
    print("Content-Type:", resp.headers.get("Content-Type"))
    data = json.loads(resp.read().decode("utf-8"))

print("\nid:      ", data["id"])
print("name:    ", data["name"])
print("username:", data["username"])
print("email:   ", data["email"])
print("city:    ", data["address"]["city"])
print("company: ", data["company"]["name"])
