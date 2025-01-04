import requests

access_token=""
api_url = "https://api.dribbble.com/v2/user"
headers = {"Authorization":f"Bearer {access_token}"}

response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    user_data = response.json()
    print(user_data)
    print(f"Nazwa uzytkownika: {user_data['name']}")
    print(f"Email: {user_data['email']}")
    print(f"Ilosc zlapanych zdjec: {user_data['shots_count']}")
else:
    print("Błąd przy pobieraniu danych: ", response.json())