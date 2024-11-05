from http.client import responses

import requests
from data import Data

class OrderMethods:

    def create_order(params):
        response = requests.post(f"{Data.BASE_URL}{Data.ORDERS_URL}", json=params)
        return response.status_code, response.text

    def get_order_list():
        response = requests.get(f"{Data.BASE_URL}{Data.ORDERS_URL}")
        return response.status_code, response.text