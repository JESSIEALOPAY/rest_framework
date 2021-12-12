import requests
from pprint import pprint

def client():
    token = "Token d9e804ca2c672c575c7af311bfa989fbb36f1d32"

    headers = {
        "Authorization": token,
    }
    response = requests.get(
        url = "http://127.0.0.1:5000/api/profile-list/",
        headers = headers,
    )

    print(f"Status Code: {response.status_code}")
    response_data = response.json()
    pprint(response_data)

if __name__ == "__main__":
    client()