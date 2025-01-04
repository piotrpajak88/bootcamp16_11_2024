import requests

client_id = "33922da0276c3d7ea257ba32ab1a1c57150aaed18779ffb9d09d97ead76ca3c1"
token_url = "https://dribbble.com/oauth/token"
client_secret = "459233ae2099dc33a0e399a97e128aad8bf41bffd18dd67675f210104cb591de"

auth_code = input("Wklej kod autoryzacyjny: ")

response = requests.post(
    token_url,
    headers={"Accept": "application/json"},
    data={
        "client_id": client_id,
        "client_secret": client_secret,
        "code": auth_code,
        "grant_type": "authorization_code",
    },
)

if response.status_code == 200:
    print(response.json())
else:
    print("Blad w uzyskaniu tokenu",response.json())
