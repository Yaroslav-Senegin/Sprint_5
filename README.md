# Финальный проект 5 спринта

## Фикстуры: файл ***conftest.py***

* `driver` - настройки webdriver

## Данные пользователя и список имейлов не по формату: файл ***data.py***

* `class Data` - Данные пользователя для корректных логинов
* `class UrlList` - Список URL для перехода на нужные страницы
  

## Вспомогательные функции: файл ***helper_functions.py***

* `random_name` - Метод генерирует имя из букв латинского алфавита
* `random_email` - Метод генерирует имейл из букв латинского алфавита и цифр
* `random_pass` - Метод генерирует пароль из букв латинского алфавита и цифр. Длинной - шесть символов 
* `mail_with_name_only` - Метод генерирует имейл только с именем почтового ящика
* `mail_with_error_domain` - Метод генерирует имейл с ошибкой в домене 


## Тесты


### Проверки регистрации пользователя: файл ***test_1_registration.py***

* `test_registration_without_name` - Попытка регистрации без имени
* `test_registration_without_email` - Попытка регистрации без имейла
* `test_registration_without_pass` - Попытка регистрации без пароля
* `test_registration_password_less_6_synbols` - Попытка регистрации с паролем <6 символов. Проверяем граничные значения 1 и 5
* `test_registration_with_incorrect_email` - Регистрация пользователя с имейлом не по формату
* `test_registration_correct` - Успешная регистрация
* `test_registration_with_exist_user` - Попытка регистрации уже существующего пользователя


### Проверки логина пользователя: файл ***test_2_login.py***

* `test_login_from_main_page` - Логин с главной страницы
* `test_login_from_account` - Логин со страницы личного кабинета
* `test_login_from_login_page` - Логин со страницы логина
* `test_login_after_registration` - Логин сразу после регистрации
* `test_login_from_recovery_pass` - Логин со страницы восстановления пароля


### Проверка перехода в личный кабинет : файл ***test_3_go_to_account_from_main.py***

* `test_go_to_account_from_main` - Переход по клику на «Личный кабинет» с главной страницы


### Проверка перехода из личного кабинета в конструктор : файл ***test_4_go_to_constructor_from_account.py***

* `test_go_to_constructor_from_account` - Переход по клику на «Конструктор» и на логотип Stellar Burgers


### Проверка выхода из аккаунта: файл ***test_5_logout.py***

* `test_logout` - Выход по кнопке «Выйти» в личном кабинете


### Взаимодействие с конструктором бургеров: файл ***test_6_constructors.py***

* `test_go_to_souses` - Переход во вкладку "Соусы"
* `test_go_to_nachinki` - Переход во вкладку "Начинки"
* `test_go_to_bulki` - Переход во вкладку "Булки" через "Начинки"
