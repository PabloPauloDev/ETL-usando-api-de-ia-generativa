import pandas as pd
import requests
import json

df = pd.read_csv('SDW2023EX.csv')
sdw_api = 'https://sdw-2023-prd.up.railway.app'
user_ids = df['UserID'].tolist()



def get_user(id):
    response = requests.get(f'{sdw_api}/users/{id}')
    return response.json() if response.status_code == 200 else None



users = [user for id in user_ids if (user := get_user(id)) is not None]