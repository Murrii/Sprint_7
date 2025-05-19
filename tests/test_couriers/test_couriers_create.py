import pytest
import data
from methods.courier_methods import CourierMethods
import allure


class TestCreateCourier:
    @allure.title("Успешное создание курьера")
    @allure.description("Передаем все необходимые параметры. Проверяем, что пришел успешный статус и тело ответа не пустое.")
    def test_creation_courier_all_params_send_status_code_201(self):
        courier = CourierMethods()
        status_code, json = courier.create_courier()
        assert status_code == 201 and json == {"ok": True}
        # удаляем курьера после получения результатов теста
        courier.after_assert_delite_courier()

    @allure.title("Нельзя создать курьера, не передав все обязательные поля")
    @allure.description("При помощи параметризации проводим два теста, для каждого из которых передаем payload без обязательного параметра")
    @pytest.mark.parametrize("payload", [ data.COURIER_WITHOUT_LOGIN, data.COURIER_WITHOUT_PASSWORD])
    def test_creation_courier_with_not_all_params_send_status_code_400(self, payload):
        courier = CourierMethods()
        status_code, json = courier.create_courier(payload)
        assert (status_code == 400 and
                json["message"] == "Недостаточно данных для создания учетной записи")
        # удаляем курьера после получения результатов теста
        courier.after_assert_delite_courier()

    @allure.title("Нельзя создать не уникального курьера")
    @allure.description("Создаем уникального курьера и пытаемся создать еще одного курьера с теми же данными")
    def test_creation_not_unic_courier_status_code_409(self):
        courier = CourierMethods()
        # создаем уникального курьера
        courier.create_courier()
        # пытаемся создать еще одного курьера с такими же данными
        status_code, json = courier.create_courier()
        assert status_code == 409 and json["message"] == "Этот логин уже используется. Попробуйте другой."
        # удаляем курьера после получения результатов теста
        courier.after_assert_delite_courier()