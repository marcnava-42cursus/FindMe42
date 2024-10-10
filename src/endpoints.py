# src/endpoints.py
from src import APIClient
from config import BASE_URL, API_VERSION

def get_user_data(user_id):
    client = APIClient()
    url = f"{BASE_URL}/{API_VERSION}/users/{user_id}"
    
    return client.get(url)
