import requests
import pytest

api_url = "https://jsonplaceholder.typicode.com"

def test_get_posts():
    # Проверка GET /posts
    response = requests.get(f"{api_url}/posts")
    assert response.status_code == 200  # Убеждаемся, что получен код 200 (успешно)
    assert len(response.json()) > 0  # Проверяем, что полученный ответ содержит непустой список постов

def test_create_post():
    # Проверка POST /posts
    data = {
        "title": "Test Title",
        "body": "Test Body",
        "userId": 1
    }
    response = requests.post(f"{api_url}/posts", json=data)
    assert response.status_code == 201  # Убеждаемся, что создание поста прошло успешно с кодом 201 (успешное создание)
    assert response.json()["title"] == data["title"]  # Проверяем, что созданный пост содержит ожидаемый заголовок
    assert response.json()["body"] == data["body"]  # Проверяем, что созданный пост содержит ожидаемое содержимое
    assert response.json()["userId"] == data["userId"]  # Проверяем, что созданный пост содержит ожидаемый userId

def test_delete_post():
    # Проверка DELETE /posts
    response = requests.delete(f"{api_url}/posts/1")
    assert response.status_code == 200  # Убеждаемся, что удаление поста прошло успешно (код 200)
    assert response.json() == {}  # Проверяем, что удаленный пост не содержит данных

    response = requests.get(f"{api_url}/posts/1")
    assert response.status_code == 404  # Убеждаемся, что пост с указанным id больше не существует (код 404)
