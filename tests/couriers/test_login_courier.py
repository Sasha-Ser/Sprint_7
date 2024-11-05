import pytest
import allure
from data import Data
from methods.courier_methods import CourierMethods


class TestLoginCourier:

    @allure.title('Проверка успешной авторизации курьера')
    def test_login_courier_true(self, courier):
        CourierMethods.create_courier(Data.COURIER_DATA_SIGNIN)
        status_code, response_context = CourierMethods.login_courier(Data.COURIER_DATA_SIGNIN)
        courier_id = CourierMethods.get_courier_id(Data.COURIER_DATA_SIGNIN)
        assert status_code == 200 and response_context == '{"id":' + f"{courier_id}" + '}'

    @allure.title('Проверка авторизации курьера без логина')
    def test_login_courier_without_login_true(self, courier):
        CourierMethods.create_courier(Data.COURIER_DATA_SIGNIN)
        status_code, response_context = CourierMethods.login_courier(Data.COURIER_DATA_WITHOUT_LOGIN)
        assert status_code == 400

    @allure.title('Проверка авторизации курьера без пароля')
    def test_login_courier_without_pass_true(self, courier):
        CourierMethods.create_courier(Data.COURIER_DATA_SIGNIN)
        status_code, response_context = CourierMethods.login_courier(Data.COURIER_DATA_WITHOUT_PASS)
        assert status_code == 504

    @allure.title('Проверка авторизации несуществующего курьера')
    def test_login_non_existent_courier_true(self):
        status_code, response_context = CourierMethods.login_courier(Data.COURIER_DATA_SIGNIN)
        assert status_code == 404


