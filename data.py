ORDERS_URL = "https://qa-scooter.praktikum-services.ru/api/v1/orders"
COURIERS_URL = "https://qa-scooter.praktikum-services.ru/api/v1/courier"

STABLE_DATA_COURIER = {
    "login": "ktrof3344",
    "password": "ktrof3344"
}

COURIER_WITHOUT_LOGIN = {
    "password": "ktrof_password1122"
}
COURIER_WITHOUT_PASSWORD = {
    "login": "ktrof_login1122"
}

ORDER_WITH_BLACK_COLOR = {
    "firstName": "Шерлок",
    "lastName": "Холмс",
    "address": "Бэйкер-стрит, 221б",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2026-06-06",
    "comment": "Элементарно, Ватсон!",
    "color": [
        "BLACK"
    ]
}

ORDER_WITH_GREY_COLOR = {
    "firstName": "Доктор",
    "lastName": "Ватсон",
    "address": "Бэйкер-стрит, 221б",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2026-06-06",
    "comment": "Что мне делать в Лондоне, сэр?",
    "color": [
        "GREY"
    ]
}

ORDER_WITH_BLACK_AND_GREY_COLOR = {
    "firstName": "Миссис",
    "lastName": "Хадсон",
    "address": "Бэйкер-стрит, 221б",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2026-06-06",
    "comment": "Не желаете ли чашечку чая?",
    "color": [
        "GREY", "BLACK"
    ]
}

ORDER_WITH_NO_COLOR = {
    "firstName": "Профессор",
    "lastName": "Мориарти",
    "address": "Бэйкер-стрит, 221б",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2026-06-06",
    "comment": "Не желаете ли чашечку чая?",
    "color": []
}