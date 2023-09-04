import requests
import json
from Extraction import sdw_api

def update_user(user):
    response = requests.put(f"{sdw_api}/users/{user['id']}", json=user)
    return True if response.status_code == 200 else False