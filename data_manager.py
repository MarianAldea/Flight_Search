import requests
import os
class DataManager:
    def __init__(self):
        self.api_endpoint = "https://api.sheety.co/0b4ea8ceb1c8266acbcd3af518e0c361/flightDeals/prices"
        self.api_header = {
                            "Authorization":os.environ.get("SHEETY_API_KEY")
        }
        self.read_response = None
        self.price_list = []
        self.users_endpoint = "https://api.sheety.co/0b4ea8ceb1c8266acbcd3af518e0c361/flightDeals/users"
        self.users_get = "https://api.sheety.co/0b4ea8ceb1c8266acbcd3af518e0c361/flightDeals/users"



    def read_data(self):
        self.sheet_data = requests.get(url=self.api_endpoint,headers=self.api_header )
        print (self.sheet_data.json())
        self.price_list = self.sheet_data.json()["prices"]
        return self.price_list


    def write_iata(self, code,id):
        iata_params = {
            "price":code

            }

        response = requests.put(url=f"{self.api_endpoint}/{id}", headers=self.api_header,json=iata_params)
        print(f"{self.api_endpoint}/{id}")
        print(response.text)

    def post_users(self,f_name, l_name, email):
        user_params = {
            "user":{
                "firstName":f_name,
                "lastName":l_name,
                "email":email,

            }
        }
        post_get = requests.get(url=self.users_get, headers=self.api_header, json=user_params)
        post_response = requests.post(url=self.users_endpoint, headers=self.api_header, json=user_params)
        print(post_response.text)
        print(post_get.text)

    def get_users(self):
        post_get = requests.get(url=self.users_get, headers=self.api_header)
        return post_get.json()