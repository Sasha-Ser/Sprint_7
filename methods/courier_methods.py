from http.client import responses

import requests
from data import Data

class CourierMethods:

    def create_courier(params):
        response = requests.post(f"{Data.BASE_URL}{Data.COURIERS_URL}", data=params)
        return response.status_code, response.text

    def delete_courier(params):
        response = requests.post(f"{Data.BASE_URL}{Data.COURIERS_URL}{Data.LOGIN_URL}",data=params)
        courier_id = response.json()["id"]
        response_del = requests.delete(f"{Data.BASE_URL}{Data.COURIERS_URL}{courier_id}")

    def login_courier(params):
        response = requests.post(f"{Data.BASE_URL}/courier/login", data=params)
        return response.status_code, response.text

    def get_courier_id(params):
        response = requests.post(f"{Data.BASE_URL}{Data.COURIERS_URL}{Data.LOGIN_URL}", data=params)
        courier_id = response.json()["id"]
        return courier_id