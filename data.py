class Data:

    BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'
    ORDERS_URL = 'orders'
    COURIERS_URL = 'courier/'
    LOGIN_URL = 'login/'

    COURIER_DATA_SIGNIN = {
    "login": "saske_00901",
    "password": "1234",
    "firstName": "saske"
}
    COURIER_DATA_WITHOUT_LOGIN = {
        "password": "1234"
    }

    COURIER_DATA_WITHOUT_PASS = {
        "login": "saske_00901"
    }

    ORDER_BLACK_COLOR = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK"
        ]
    }
    ORDER_GREY_COLOR = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "GREY"
        ]
    }
    ORDER_BOTH_COLORS = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "GREY",
            "BLACK"
        ]
    }
    ORDER_WITHOUT_COLOR = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha"
    }

