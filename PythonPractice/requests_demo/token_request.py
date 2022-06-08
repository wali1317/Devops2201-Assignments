import requests
import json
# import base
import os
import base64


url = 'https://izaan-test.auth.us-east-1.amazoncognito.com/oauth2/token'

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path + '/secret.json') as json_data:
    secrets = json.load(json_data)
    print(secrets)


def get_token():
    print('Get Token')
    payload = "scope=izaan_test%2Fpost_info&grant_type=client_credentials"
    user_name = secrets['userName']
    password = secrets['password']
    credentials = encode_base64(user_name, password)
    headers = {
        "Authorization": "Basic " + credentials,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = requests.request("POST", url=url, data=payload, headers=headers)
    # print(type(response))
    # print(response)
    # print(type(response.text))
    # print()
    response_as_dict = json.loads(response.text)
    print(response_as_dict)
    access_token = response_as_dict['access_token']
    return access_token


# """
# curl --location --request POST 'https://5x9m5ed0tj.execute-api.us-east-1.amazonaws.com/test/submit' \
# --header 'Content-Type: application/json' \
# --header 'Authorization: Bearer eyJraWQiOiJtNlhhM3FkczlxY2o2ODZYOVBRb0JqTEJSQU5yMzBPZ21ZQzdvdThZc1N3PSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIxdTVpbzR2YTlzcjQ1bjc5ZmNlZzJkYW1qZiIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiaXphYW5fdGVzdFwvcG9zdF9pbmZvIiwiYXV0aF90aW1lIjoxNjU0MDMyODE0LCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9ZN3k4cTVDMVoiLCJleHAiOjE2NTQwMzY0MTQsImlhdCI6MTY1NDAzMjgxNCwidmVyc2lvbiI6MiwianRpIjoiOWUyZjZkOGYtMmI5ZS00MzRiLTkzMWUtOTQ0YTI5NTNjY2EyIiwiY2xpZW50X2lkIjoiMXU1aW80dmE5c3I0NW43OWZjZWcyZGFtamYifQ.Hs7qA4cnFEpZlV0F2-eZWnMaXwxOQbFTzNQFfHL3sgph1l7l7aF8MWWzvJrFYARYOro1VEuUWpo_mCqHTUCRTwazhCk2KCX5qnOnZiWRF8LcukS8PO8sYIUNp3zlG0RSa6GUz5eJXCUQhNBHnMursVy4gyv4xWAcn29kLEmWTnl2S0UAZCSdYHzEhsn8eMy4I5-Ibgzvuz3k9GFUB3TpSjqjajk1nKe9v8SwcEjOqtpGp5BuULaDM6G2-6oOOERXP-v5VGdQEuAa5kTHxwe5lGumTPxUVih-3GQxBQE-mMUCdfb21sMekBnUbzT3HkTuaHJVBD5P8AoeEPyeyOayRw' \
# --data-raw '{
# 	"name" : "John",
# 	"age" : 50
# }'
# """


# def find_who_you_are():
#     # Please use above info to make a post call by your own
#     print("Make a post call, get to know if you are an Adult!!!")


def encode_base64(user_name, password):
    message = user_name + ":" + password
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    print(base64_message)
    return base64_message


def decode_base64():
    base64_message = ""
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    print(message)


if __name__ == "__main__":
    # encoded_value = encode_base64("Jahidul", "Islam")
    # print(encoded_value)
    token = get_token()
    print(token)
