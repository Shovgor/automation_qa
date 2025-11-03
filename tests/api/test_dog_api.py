import pytest
from src.api.clients.dog_api_client import DogApiClient


@pytest.mark.parametrize("endpoint", [
    "/breeds/list/all",
    "/breed/hound/images",
    "/breeds/image/random",
])
def test_dog_api_success(endpoint):
    response = DogApiClient().get(endpoint=endpoint)
    assert response.status_code == 200
    assert response.json()["status"] == "success"


def test_random_image_is_valid_url():
    response = DogApiClient().get("/breeds/image/random")
    data = response.json()
    assert data["status"] == "success"
    assert data["message"].startswith("https")
