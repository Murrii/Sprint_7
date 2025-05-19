import allure
import pytest
import data
from methods.orders_methods import OrderMethods


class TestOrderCreate:
    @allure.title("Создание заказа с разными вариантами цвета самоката (параметризация)")
    @pytest.mark.parametrize("payload", [data.ORDER_WITH_NO_COLOR,
                                         data.ORDER_WITH_BLACK_COLOR,
                                         data.ORDER_WITH_GREY_COLOR,
                                         data.ORDER_WITH_BLACK_AND_GREY_COLOR])
    def test_create_order_with_any_color_status_code_201(self, payload):
        order = OrderMethods()
        status_code, json = order.post_create_order(payload)
        assert status_code == 201 and "track" in str(json)

    @allure.title("Получение списка заказов")
    def test_get_order_list_status_code_200(self):
        order = OrderMethods()
        _, json = order.post_create_order(data.ORDER_WITH_NO_COLOR)
        get_orders_list_status_code, order_list_json = order.get_orders_list()
        assert get_orders_list_status_code == 200 and len(order_list_json["orders"]) != 0