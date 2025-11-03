import requests
import config


class DogApiClient:
    """Reusable client for Dog API endpoints."""

    def __init__(self):
        self.url = config.DOG_API_URL

    def get(self, endpoint: str, params=None):
        url = f"{self.url.rstrip('/')}/{endpoint.lstrip('/')}"
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response

    def post(self, endpoint: str, data=None, json=None):
        url = f"{self.url.rstrip('/')}/{endpoint.lstrip('/')}"
        response = requests.post(url, data=data, json=json)
        response.raise_for_status()
        return response
