from data import COURIERS_URL as url
import requests
import string
import random
import allure


class CourierMethods:
    # генератор случайной строки
    @staticmethod
    def generate_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @allure.step("Создаем экземпляр курьера. При создании - генерируем логин, пароль и имя")
    # сохраняем данные пользователя в атрибутах экземпляра класса для удобного обращения к ним и генерации payload-ов
    # к случайной строке добавлен личный префикс, чтобы минимизировать пересечение с другими учениками
    def __init__(self):
        self.login = 'ktrof_' + self.generate_string(10)
        self.password = 'ktrof_' + self.generate_string(10)
        self.name = 'ktrof_' + self.generate_string(10)

        # данные для регистрации курьера
        self.payload_for_create = {
            "login": self.login,
            "password": self.password,
            "firstName": self.name
        }
        # данные для авторизации курьера
        self.payload_for_login = {
            "login": self.login,
            "password": self.password
        }

    @allure.step("Создаем курьера в приложении.")
    # Данные для создания по умолчанию берем из экземпляра класса, но оставляем возможность передать свой payload для негативных кейсов
    def create_courier(self, payload = None):
        if payload is None:
            payload = self.payload_for_create
        response = requests.post(f"{url}", json = payload)
        return response.status_code, response.json()


    @allure.step("Авторизируемся в приложении, получаем id")
    # По умолчанию используем сгенерированные для экземпляра данные. Возвращаем id курьера
    def login_courier(self, payload = None):
        if payload is None:
            payload = self.payload_for_login
        response = requests.post(f"{url}/login", json=payload)
        return response.status_code, response.json()

    @allure.step("Удаляем курьера с переданным id")
    def delete_courier(self, current_id):
        payload = {"id": current_id}
        response = requests.delete(f"{url}/{current_id}", json = payload)
        return response.status_code, response.json()

    @allure.step("Удаляем курьера после выполнения теста")
    def after_assert_delite_courier(self):
        self.delete_courier(self.login_courier())