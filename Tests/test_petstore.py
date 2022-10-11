import requests
import pytest

pet_ID = 42
response = requests.get(f"https://petstore.swagger.io/v2/pet/{pet_ID}")


def test_find_pet_by_ID():
    assert response.status_code == 200


def test_name_pet():
    name_pet = "Kotka"
    assert response.json()["name"] == name_pet
