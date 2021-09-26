import urllib
import uuid
import hmac
import hashlib
import base64
from urllib.parse import quote
import requests
from django.conf import settings


def get_user_id(username):
        base_url = f"https://api.twitter.com/2/users/by/username/{username}"

        bearer_token = settings.TWITTER_BEARER_TOKEN
        headers = {
                "Authorization": f'Bearer {bearer_token}',
                }
        response = requests.get(base_url, headers=headers)
        print(response.json())
        print(response.status_code)
        if response.ok:
            try:
                data = response.json()
                user_id = data["data"]["id"]
                print(user_id)
                return user_id
            except:
                return None
        else:
            print("NOT OKAY")
            return None
            
