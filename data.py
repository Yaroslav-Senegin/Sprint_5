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


# Список имейлов не по формату для проверки регистрации с корректным имейлом
unform_email = [f"{''.join(random.choice(string.ascii_lowercase) for i in range(10))}_{random.randint(3000, 3999)}",
                f"{''.join(random.choice(string.ascii_lowercase) for i in range(10))}_{random.randint(3000, 3999)}@yandex."]
