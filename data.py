import random
import string

# Данные пользователя для корректных логинов
class Data:
    name = 'Yar'
    email = 'yar_senegin_3123@yandex.ru'
    password = 'Test123!'

# Список имейлов не по формату для проверки регистрации с корректным имейлом
unform_email = [f"{''.join(random.choice(string.ascii_lowercase) for i in range(10))}_{random.randint(3000, 3999)}",
                f"{''.join(random.choice(string.ascii_lowercase) for i in range(10))}_{random.randint(3000, 3999)}@yandex."]
