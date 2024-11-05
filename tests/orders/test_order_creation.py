import pytest
import allure
from data import Data

from methods.order_methods import OrderMethods

class TestOrderCreate:

    orders = [
        Data.ORDER_BOTH_COLORS,
        Data.ORDER_WITHOUT_COLOR,
        Data.ORDER_BLACK_COLOR,
        Data.ORDER_GREY_COLOR
    ]

    @allure.title('Проверка создания заказа')
    @pytest.mark.parametrize("orders", orders)
    def test_creation_order(self, orders):
        status_code, response_context = OrderMethods.create_order(orders)
        assert status_code == 201 and "track" in response_context
