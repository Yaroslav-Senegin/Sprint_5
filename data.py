import random
import string

# Данные пользователя для корректных логинов
class Data:
    name = 'Yar'
    email = 'yar_senegin_3123@yandex.ru'
    password = 'Test123!'


# Список URL для перехода на нужные страницы
class UrlList:
    page_main_url = 'https://stellarburgers.nomoreparties.site/'  # URL главной страницы Конструктор
    page_login_url = 'https://stellarburgers.nomoreparties.site/login' # URL страницы логин
    page_registration_url = 'https://stellarburgers.nomoreparties.site/register'  # URL страницы регистрации
