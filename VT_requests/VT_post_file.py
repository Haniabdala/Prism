import requests

url = "https://www.virustotal.com/api/v3/files"

def Post_file(file_path,file_type,API_KEY):

    files = {"file": (file_path, open(file_path, "rb"), file_type)}
    headers = {
    "accept": "application/json",
    "x-apikey": API_KEY
    }

    response = requests.post(url, files=files, headers=headers)

    print(response.text)