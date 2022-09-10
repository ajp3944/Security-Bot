import requests

def get_hash(user_input):
    ip_address = user_input
    response = requests.get(f'https://freerestapi.herokuapp.com/api/hash-identifier?hash={user_input}').json()
    hash_data = {
        "Hash": response.get("hash"),
        "Hash Type": response.get("hash_type"),
        "Bit Length": response.get("bit_length"),
        "Character Length": response.get("char_length"),
        "Character Type": response.get("char_type"),

    }
    return hash_data

print(get_hash(""))