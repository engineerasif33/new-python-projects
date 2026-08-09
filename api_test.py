import requests

url = "https://jsonplaceholder.typicode.com/users"


# -------- GET: Get data --------

response = requests.get(url)

if response.status_code == 200:
    users = response.json()

    print("GET Request:")
    print("First User:", users[0]["name"])


# -------- POST: Create new data --------

new_user = {
    "name": "muhammad asif",
    "email": "engineerasif33@gmail.com"
}

response = requests.post(url, json=new_user)

if response.status_code == 201:
    user = response.json()

    print("\nPOST Request:")
    print("New User:", user["name"])
    print("Email:", user["email"])
    print("User ID:", user["id"])


# -------- PUT: Update existing data --------

update_url = "https://jsonplaceholder.typicode.com/users/1"

updated_user = {
    "name": "Ahmed",
    "email": "ahmed@example.com"
}

response = requests.put(update_url, json=updated_user)

if response.status_code == 200:
    user = response.json()

    print("\nPUT Request:")
    print("Updated Name:", user["name"])
    print("Updated Email:", user["email"])