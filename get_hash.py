from turtle import up
import requests
import hashlib

file_url = 'https://cdn.discordapp.com/attachments/1018003056077574195/1018245724552564888/sillyfile.txt'
api_key = '93d85cbb593276a2a1eec152078bcd97df0c84ff42bd092b14455aa9ff152b3f'

## Searches the type of hash
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

## Used for uploading file to virustotal
def upload_file(file):
    data = requests.get(file)
    hash = hashlib.sha256(data.text.encode('UTF-8')).hexdigest()
    file = {"file": data.text}
    url = f'https://www.virustotal.com/api/v3/files'
    headers = {"Accept": "application/json", "x-apikey":api_key}
    response = requests.post(url, files=file, headers=headers)

    return hash

## Used for retrieving information about a file from virustotal
def file_info():
    id = upload_file(file_url)
    url = f'https://www.virustotal.com/api/v3/files/{str(id)}'
    print(url)
    headers = {"Accept": "application/json", "x-apikey":api_key}
    response = requests.get(url, headers=headers)
    print(response.text)


file_info()