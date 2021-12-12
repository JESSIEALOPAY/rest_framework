import requests
from pprint import pprint

def client():
    credentials = {
        "username": "salla_gitsin",
        "password": "yoruldum"
    }
    # credentials = {
    #     "username": "burak",
    #     "password": "123456"
    # }

    response = requests.post(
        url = "http://127.0.0.1:5000/api/rest-auth/login/",
        data = credentials        
    )

    print(f"Response Status Code: {response.status_code}")
    response_data = response.json()
    pprint(response_data)

if __name__ == "__main__":
    client()
