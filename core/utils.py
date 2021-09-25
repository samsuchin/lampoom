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
        if response.ok:
            data = response.json()
            user_id = data["data"]["id"]
            print(user_id)
            return user_id
            

def encode(s):
    return quote(s, safe='')

def generate_signature(oauth_consumer_key, nonce, oauth_token, timestamp, base_url, oauth_consumer_secret, oauth_token_secret, screen_name):
    key_pair = {
        "include_entities": "true",
        "oauth_consumer_key": oauth_consumer_key,
        "oauth_nonce": nonce,
        "oauth_signature_method": "HMAC-SHA1",
        "oauth_timestamp": timestamp,
        "oauth_token": oauth_token,
        "oauth_version": "1.0",
        "screen_name": screen_name
    }

    key_pair = dict((encode(k), encode(v)) for (k, v) in key_pair.items())
    parameter_string = ""
    for k, v in sorted(key_pair.items()):
        parameter_string += f"{k}={v}&"
    parameter_string = parameter_string[:-1]
    print(parameter_string)
    signature_base_string = bytes(f"GET&{encode(base_url)}&{encode(parameter_string)}", "ascii")
    print(signature_base_string)
    signing_key = bytes(f"{encode(oauth_consumer_secret)}&{encode(oauth_token_secret)}", "ascii")
    hashed = hmac.new(signature_base_string, signing_key, hashlib.sha1)
    output = base64.b64encode(hashed.digest()).decode()
    print(output)
    return output
