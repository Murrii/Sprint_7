import pytest
from methods.courier_methods import CourierMethods
import allure

@pytest.fixture
@allure.title("Создаем экземпляр класса Курьер. После окончания теста - удаляем созданного курьера")
def courier():
    # создаем экземпляр класса CourierMethods
    courier = CourierMethods()
    yield courier
    courier.after_assert_delite_courier()