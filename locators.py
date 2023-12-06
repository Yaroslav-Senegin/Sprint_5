from selenium.webdriver.common.by import By


class Locators:
    page_main_url = 'https://stellarburgers.nomoreparties.site/'  # URL главной страницы Конструктор
    page_login_url = 'https://stellarburgers.nomoreparties.site/login' # URL страницы логин
    page_registration_url = 'https://stellarburgers.nomoreparties.site/register'  # URL страницы регистрации
    login_button_main = By.XPATH, './/button[text()="Войти в аккаунт"]'  # Кнопка "Войти в аккаунт" с главной страницы
    login_button_login_page = By.XPATH, './/button[text()="Войти"]'  # Кнопка "Войти" со страницы логина
    login_header_tag_h2 = By.XPATH, './/h2[text()="Вход"]'  # Заголовок "Вход"
    login_link_from_recovery_pass = By.XPATH, './/a[text()="Войти"]'  # Ссылка "Войти" со страницы восстановления пароля
    logout_button = By.XPATH, './/button[text()="Выход"]'  # Kнопка "Выход" из личного кабинета
    personal_account_button = By.XPATH, './/p[text()="Личный Кабинет"]'  # Kнопка "Личный кабинет"
    registration_button = By.XPATH, './/button[text()="Зарегистрироваться"]'  # Кнопка "Зарегистрироваться"
    recovery_pass_link = By.XPATH, './/a[text()="Восстановить пароль"]'  # Ссылка "Восстановить пароль"
    recovery_pass_button = By.XPATH, './/button[text()="Восстановить"]'  # Кнопка "Восстановить пароль"
    profile_link = By.XPATH, './/a[text()="Профиль"]'  # Ссылка "Профиль" в личном кабинете
    incorrect_pass_message = By.XPATH, './/fieldset[3]/div/p[text()="Некорректный пароль"]'  # Cообщение "Некорректный пароль"
    incorrect_pass_check = By.XPATH, './/fieldset[3]/div/p'  # Проверка сообщения "Некорректный пароль"
    user_exists_message = By.XPATH, './/div/main/div/p[text()="Такой пользователь уже существует"]'  # Сообщение "Такой пользователь уже существует"
    user_exists_check = By.XPATH, './/div/main/div/p'  # для проверки сообщения "Такой пользователь уже существует"
    input_field1 = By.XPATH, './/fieldset[1]//input'  # Поле для ввода данных
    input_field2 = By.XPATH, './/fieldset[2]//input'  # Поле для ввода данных
    input_field3 = By.XPATH, './/fieldset[3]//input'  # Поле для ввода данных
    header_h2 = By.XPATH, './/h2'  # Заголовок H2
    make_burger_tag_h1 = By.XPATH, './/section[1]/h1[text()="Соберите бургер"]'  # Заголовок "Соберите бургер" в конструкторе
    constructor_button = By.XPATH, './/p[text()="Конструктор"]'  # Kнопка "Конструктор"
    order_button = By.XPATH, './/button[text()="Оформить заказ"]'  # Kнопка "Оформить заказ"
    souses_tab = By.XPATH, './/span[text()="Соусы"]'  # Вкладка "Соусы"
    souses_check = By.XPATH, './/h2[text()="Соусы"]'  # Список "Соусы"
    nachinki_tab = By.XPATH, './/span[text()="Начинки"]'  # Вкладка "Начинки"
    nachinki_check = By.XPATH, './/h2[text()="Начинки"]'  # Список "Начинки"
    bulki_tab = By.XPATH, './/span[text()="Булки"]'  # Вкладка "Булки"
    bulki_check = By.XPATH, './/h2[text()="Булки"]'  # Список "Булки"
