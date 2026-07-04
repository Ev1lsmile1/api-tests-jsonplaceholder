import pytest
import requests

#Проверки на существующих юзеров
@pytest.mark.parametrize("user_id", [1,2,10])
def test_get_user(base_url, user_id):
    url = f"{base_url}/users/{user_id}"
    response = requests.get(url)

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == user_id
    assert data["username"]
    assert data["email"]
    assert isinstance(data, dict)

#Проверка на не существующих
@pytest.mark.parametrize("user_id", [777, 9999, 0])
def test_get_nonexistent_user(base_url, user_id):
    response = requests.get(f"{base_url}/users/{user_id}")
    assert response.status_code == 404

def test_post_user(base_url):
    url = f"{base_url}/users"
    payload = {
        "username": "test",
        "email": "asd@qwe",
        "address": "groowstreet"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 201

    data = response.json()

    assert data["username"] == "test"
    assert data["email"]
    assert "password" not in data

#Можно вместо response = requests.put ставить .patch. ПУТ удалит всю остальную инфу
# о юзере и оставит ту которую вписал. ПАТЧ только изменит значения в ключах СЛОВАРЯ
@pytest.mark.parametrize("user_id", [1,2,3])
def test_update_user(base_url, user_id):
    url = f"{base_url}/users/{user_id}"
    update_payload = {
        "username": "test",
        "email": "asd@qwe",
        "address": "groowstreet"
    }
    response = requests.put(url, json=update_payload)

    assert response.status_code == 200
    data = response.json()
    assert data["username"] == update_payload["username"]
    assert data["email"] == update_payload["email"]
    assert data["address"] == update_payload["address"]

@pytest.mark.parametrize("user_id", [1,2,3])
def test_delete_user(base_url, user_id):
    url = f"{base_url}/users/{user_id}"
    response = requests.delete(url)

    assert response.status_code == 200

    data = response.json()

    assert data == {}