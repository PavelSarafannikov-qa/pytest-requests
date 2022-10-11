import requests

response = requests.post("https://petstore.swagger.io/v2/pet", json={
    "id": 42,
    "category": {
        "id": 0,
        "name": "string"
    },
    "name": "Kotik",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": "available"
})
print(response.json())
response = requests.put("https://petstore.swagger.io/v2/pet", json={
    "id": 42,
    "category": {
        "id": 0,
        "name": "string"
    },
    "name": "Kotka",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": "available"
})
print(response.json())
pet_ID = 42
print(requests.get(f"https://petstore.swagger.io/v2/pet/{pet_ID}").json())
