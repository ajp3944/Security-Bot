import requests

def encode_32(user_input):
    response = requests.get(f'https://freerestapi.herokuapp.com/api/base32?encode={user_input}').json()
    response_data = {
        "Results": response.get("result"),
    }
    return response_data
print(encode_32('1234'))


def decode_32(user_input):
    response = requests.get(f'https://freerestapi.herokuapp.com/api/base32?decode={user_input}').json()
    response_data = {
        "Results": response.get("result"),
    }
    return response_data
print(decode_32('64t36d0'))


def encode_64(user_input):
    response = requests.get(f'https://freerestapi.herokuapp.com/api/base64?encode={user_input}').json()
    response_data = {
        "Results": response.get("result"),
    }
    return response_data
print(encode_64('1234'))


def decode_64(user_input):
    response = requests.get(f'https://freerestapi.herokuapp.com/api/base64?decode={user_input}').json()
    response_data = {
        "Results": response.get("result"),
    }
    return response_data
print(decode_64('MTIzNA=='))