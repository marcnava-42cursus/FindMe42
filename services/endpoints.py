from core.api_client import APIClient
from config import BASE_URL, API_VERSION

def get_user_data(user_id):
    client = APIClient()
    response = client.get(f"{BASE_URL}/{API_VERSION}/users/{user_id}")
    
    if isinstance(response, dict):
        return response
    elif response.status_code == 200:
        return response.json()
    return None