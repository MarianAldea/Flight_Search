from datetime import datetime
import requests
import os
class FlightData:
    def __init__(self):
        self.header = {
            "apikey":os.environ.get("FLIGHT_SEARCH_API_KEY")
        }
        self.fly_from = "LHR"
        self.api_endpoint = "https://tequila-api.kiwi.com/v2/search"
        self.date_from = None
        self.date_to = None
        self.flight_data = None
        self.city = None
        self.price = None
        self.complete_list = []

    def check_flights(self ):
        self.check_datetime()
        self.api_params = {
            "fly_from":self.fly_from,
            "fly_to":self.city,
            "date_from":self.date_from,
            "date_to":self.date_to,

        }

        response = requests.get(url=self.api_endpoint, params=self.api_params, headers=self.header)
        # print(response.json())
        self.flight_data = response.json()["data"]

        # print(flight_data)

    def check_datetime(self):
        dt = datetime.now()
        self.date_from = dt.strftime("%d/%m/%Y")
        date = self.date_from.split("/")
        if int(date[1]) < 7:
            date[1] = int(date[1]) + 6
        else:
            date[1] = int(date[1]) + 6 - 12
            date[2] = int(date[2]) + 1
        self.date_to = str(date[0])+"/"+str(date[1])+"/"+str(date[2])


    def compare_prices(self, city, price):
        self.complete_list = []
        self.city = city
        self.price = price
        self.check_flights()
        for i in self.flight_data:
            if int(i["price"])*1.16 < self.price:
                self.complete_list.append(f"Flight to {i['cityCodeTo']}, {i['cityTo']} is {i['price']} euros and leaves at"
                      f" {i['local_departure'].split('T')[0]}")
        return(self.complete_list)


