import allure
import requests
from data import ORDERS_URL as url


class OrderMethods:
    def __init__(self):
        self.url = url

    @allure.step("Создаем заказ")
    def post_create_order(self, payload):
        response = requests.post(self.url, json = payload)
        return response.status_code, response.json()

    @allure.step("Получаем список заказов")
    def get_orders_list(self):
        response = requests.get(self.url)
        return response.status_code, response.json()


