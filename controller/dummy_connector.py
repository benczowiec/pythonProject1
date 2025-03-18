
import requests
import logging

class DummyConnector:

    base_url ="https://dummyjson.com/"
    endpoint = "users"


    def get_user_info(self, skip, limit):
        url = f"{self.base_url}{self.endpoint}?skip={skip}&limit={limit}"
        response = requests.get(url)

        if response.status_code == 200:
            print("\n************ SUCCESSFULLY FETCHED DATA ************\n")
            # logging.info("Successfully fetched data")
            return response.json()
        else:
            logging.info("Request failed to fetch data")
