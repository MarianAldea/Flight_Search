import requests
import os
class FlightSearch:
    def __init__(self):
        self.api_key = os.environ.get("FLIGHT_SEARCH_API_KEY")
        self.api_endpoint = "https://tequila-api.kiwi.com/locations/query"
        self.search_data = None
        self.header = {"apikey":self.api_key}




    def find_iata(self, city):
        self.city = city
        self.api_params = {
                           "term": self.city,
                           "location_type": "city",
                           "limit": "20",
                           }
        self.search_data = requests.get(url=self.api_endpoint, params=self.api_params, headers=self.header).json()
        return self.search_data