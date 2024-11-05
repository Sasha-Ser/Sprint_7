import pytest

from methods.courier_methods import CourierMethods
from data import Data


@pytest.fixture()
def courier():
    yield
    CourierMethods.delete_courier(Data.COURIER_DATA_SIGNIN)
