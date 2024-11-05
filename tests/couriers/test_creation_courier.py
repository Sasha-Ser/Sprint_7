from methods.courier_methods import CourierMethods
from data import Data
import allure


class TestCreationCourier():

    @allure.title('Проверка успешного создания курьера')
    def test_creation_courier(self, courier):
        status_code, response_context = CourierMethods.create_courier(Data.COURIER_DATA_SIGNIN)
        assert status_code == 201 and response_context == '{"ok":true}'

    @allure.title('Проверка создания дубликата курьера')
    def test_creation_copy_of_courier_true(self, courier):
        CourierMethods.create_courier(Data.COURIER_DATA_SIGNIN)
        status_code, response_context = CourierMethods.create_courier(Data.COURIER_DATA_SIGNIN)
        assert status_code == 409

    @allure.title('Проверка создания курьера без логина')
    def test_creation_courier_without_login(self):
        status_code, response_context = CourierMethods.create_courier(Data.COURIER_DATA_WITHOUT_LOGIN)
        assert status_code == 400

    @allure.title('Проверка создания курьера без пароля')
    def test_creation_courier_without_pass(self):
        status_code, response_context = CourierMethods.create_courier(Data.COURIER_DATA_WITHOUT_PASS)
        assert status_code == 400
