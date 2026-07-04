import pytest
import requests

@pytest.mark.parametrize("post_id", [1,2,3,4])
def test_exist_post(base_url,post_id):
    url = base_url + f'/posts/{post_id}'
    response = requests.get(url)
    assert response.status_code == 200

    data = response.json()

    assert data["id"] == post_id
    assert data["title"]

@pytest.mark.parametrize("post_id", [0,101,888])
def test_not_exist_post(base_url,post_id):
    url = base_url + f'/posts/{post_id}'
    response = requests.get(url)
    assert response.status_code == 404

@pytest.mark.parametrize("user_id", [1,2,3,4])
def test_create_post(base_url,user_id):
    url = f"{base_url}/posts"
    payload = {
        "title": "Test Post",
        "body": "Some content",
        "userId": user_id
    }

    response = requests.post(url, json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["userId"] == payload["userId"]
    assert data["title"] == payload["title"]
    assert "id" in data

@pytest.mark.parametrize("post_id", [1,2,3,4])
def test_update_post(base_url,post_id):
    url = f"{base_url}/posts/{post_id}"
    payload = {
        "title": "Updated Title",
        "body": "Updated Body",
        "userId": post_id
    }

    response = requests.put(url, json=payload)

    assert response.status_code == 200

    data = response.json()
    assert data["userId"] == payload["userId"]
    assert data["title"] == payload["title"]

@pytest.mark.parametrize("post_id", [1,2,3,4])
def test_delete_post(base_url, post_id):
    url = f"{base_url}/posts/{post_id}"

    response = requests.delete(url)

    assert response.status_code == 200

    data = response.json()
    assert data == {}