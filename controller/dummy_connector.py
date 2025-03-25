
import requests
import logging

class DummyConnector:

    base_url ="https://dummyjson.com/"


    def get_data(self, skip, limit, endpoint):
        url = f"{self.base_url}{endpoint}?skip={skip}&limit={limit}"
        response = requests.get(url)

        if response.status_code == 200:
            print("\n************ SUCCESSFULLY FETCHED DATA ************\n")
            logging.info("Successfully fetched data")
            return response.json()
        else:
            logging.info("Request failed to fetch data")
