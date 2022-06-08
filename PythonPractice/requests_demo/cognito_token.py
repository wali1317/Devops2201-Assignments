import requests
import json
# import base
import os
import base64

url = 'https://izaan-test.auth.us-east-1.amazoncognito.com/oauth2/token'


dir_path = os.path.dirname(os.path.realpath(__file__))
# print('Hello {}'.format(dir_path))
with open(dir_path + '/secret.json') as json_data:
    secrets = json.load(json_data)
    print(secrets)


def get_token():
    print('Get Token')
    payload = "grant_type=client_credentials"
    user_name = secrets['userName']
    password = secrets['password']
    credentials = encode_base64(user_name, password)
    headers = {
        "Authorization": "Basic " + credentials,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = requests.request("POST", url=url, data=payload, headers=headers)
    response_as_dict = json.loads(response.text)
    print(response_as_dict)
    access_token = response_as_dict['access_token']
    return access_token


# def find_who_you_are():
#     print("Make a post call, get to know if you are an Adult!!!")

def encode_base64(user_name, password):
    message = user_name + ":" + password
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    print(base64_message)
    return base64_message


if __name__ == '__main__':
    # encode_base64("wali", "Rashid")
    token = get_token()
    print(token)
