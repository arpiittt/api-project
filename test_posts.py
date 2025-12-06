import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_single_post_success():
    post_id = 1
    endpoint = f"{BASE_URL}/posts/{post_id}"
    print(f"\nSending GET request to: {endpoint}")

    response = requests.get(endpoint)

    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    response_data = response.json()
    print(f"Response Data: {response_data}")

    assert response_data["id"] == post_id, f"Expected post ID {post_id}, got {response_data['id']}"

    assert response_data["title"] is not None and len(response_data["title"]) > 0, "Title should not be empty"

    print("PASS: Post retrieved successfully with valid data.")

def test_get_single_post_not_found():
    post_id = 9999  # Assuming this ID does not exist
    endpoint = f"{BASE_URL}/posts/{post_id}"
    print(f"\nSending GET request to: {endpoint}")

    response = requests.get(endpoint)

    assert response.status_code == 404, f"Expected status code 404, got {response.status_code}"

    assert response.json() == {}, f"Expected empty response body, got {response.json()}"

    print("PASS: Correctly received 404 for non-existent post.")

def test_create_new_post():
    endpoint = f"{BASE_URL}/posts"
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }

    headers = {
        "Content-type": "application/json"
    }

    print(f"\nSending POST request to: {endpoint} with payload: {payload}")

    response = requests.post(endpoint, json=payload, headers=headers)

    assert response.status_code == 201, f"Expected status code 201, got {response.status_code}"

    response_data = response.json()
    print(f"Response Data: {response_data}")

    assert "id" in response_data, "Response should contain an 'id' field"
    assert response_data["id"] is not None and isinstance(response_data["id"], int), \
        "FAIL: New post ID is missing or not an integer."

    print("PASS: New post created successfully with valid data.")