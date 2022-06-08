import requests
import json
import cognito_token


url = 'https://5x9m5ed0tj.execute-api.us-east-1.amazonaws.com/test/submit'


def find_who_you_are():
    print("Make a post call, get to know if you are an Adult!!!")
    raw = '{ "name" : "John", "age" : 15 }'
    credentials = cognito_token.get_token()
    headers = {
        "Authorization": "Bearer " + credentials,
        "Content-Type": "application/json"
    }
    response = requests.request("POST", url=url, data=raw, headers=headers)
    response_as_dict = json.loads(response.text)
    print(response_as_dict)
    message = response_as_dict
    return response_as_dict


if __name__ == '__main__':
    find_who_you_are()