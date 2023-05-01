from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/080db92c65c44c96aead601ec819cb21/flightDeal/price"
SHEETY_TOKEN = "*********"

bearer_headers = {
        "Authorization": f"Bearer {SHEETY_TOKEN}"
    }
class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=bearer_headers)
        data = response.json()
        self.destination_data = data["price"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
