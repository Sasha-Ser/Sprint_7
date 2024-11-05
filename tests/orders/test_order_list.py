import pytest
import allure
from methods.order_methods import OrderMethods

class TestOrderList:

    @allure.title('Проверка получения списка заказов')
    def test_order_list(self):
        status_code, response_context = OrderMethods.get_order_list()
        assert status_code == 200 and "orders" in response_context