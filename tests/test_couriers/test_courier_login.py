import pytest
import data
from methods.courier_methods import CourierMethods
import allure


class TestCourierLogin:
    @allure.title("Логин с валидными данными, возвращается id")
    def test_courier_login_with_valid_data_status_code_200(self):
        courier = CourierMethods()
        courier.create_courier()
        status_code, json = courier.login_courier()
        assert status_code == 200 and "id" in str(json)
        # так как здесь мы не передавали фикстуру, удаляющую курьера после теста, удаляем курьера вручную
        courier.after_assert_delite_courier()


    @allure.title("Логин с пропущенным обязательным полем - 400 ошибка")
    # Здесь используем данные существующего пользователя из data, но одно из полей передаем пустым
    @pytest.mark.parametrize("one_param_payload", [{"login": data.STABLE_DATA_COURIER["login"], "password": ""},
                                                   {"login": "", "password": data.STABLE_DATA_COURIER["password"]}])
    def test_courier_login_without_required_field_status_code_400(self, courier, one_param_payload):
        status_code, json = courier.login_courier(one_param_payload)
        assert status_code == 400 and json["message"] == "Недостаточно данных для входа"


    @allure.title("Логин с неправильной парой Логин/Пароль - 404 ошибка")
    # Снова используем данные существующего пользователя из data, одно из полей передаем с неверным значением
    @pytest.mark.parametrize("wrong_login_pair_payload", [{"login": data.STABLE_DATA_COURIER["login"], "password": "NonCorrectPass"},
                                                   {"login": "NonCorrectLogin", "password": data.STABLE_DATA_COURIER["password"]}])
    def test_courier_login_with_wrong_pair_pass_login_status_code_404(self, courier, wrong_login_pair_payload):
        status_code, json = courier.login_courier(wrong_login_pair_payload)
        assert status_code == 404 and json["message"] == "Учетная запись не найдена"