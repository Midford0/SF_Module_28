import pytest

from .pages.authorization_page_rt import AuthorizationPage
from .pages.password_recovery_page_rt import PasswordRecoveryPage


# проверяем что страница авторизации открывается
@pytest.mark.autorization
def test_can_open_authorization_page(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    # открываем страницу авторизации
    page.open()
    # проверяем что открылась именно страница авторизации
    page.should_be_login_page()

@pytest.mark.autorization
def test_that_telephone_email_login_account_tabs_presented_on_page(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    # открываем страницу авторизации
    page.open()
    # проверяем что на странице присутствуют табы телефон, имеил,логин,лицевой счет
    page.should_have_tabs()

@pytest.mark.autorization
def test_that_telephone_tab_is_active_by_default(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    # открываем страницу авторизации
    page.open()
    # проверяем что таб Телефон выбран по умолчанию
    page.should_have_active_telephone_tab()

@pytest.mark.autorization
def test_that_logo_is_presented(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    # открываем страницу авторизации
    page.open()
    # проверяем что на странице есть лого
    page.should_have_logo()

@pytest.mark.autorization
def test_email_tab_is_active_when_email_is_entered_in_the_field(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    # открываем страницу авторизации
    page.open()

    email = "midford0@gmail.com"
    # вводим email в поле авторизации
    page.enter_email(email)
    # проверяем что таб Имеил стал активным
    page.should_have_active_email_tab()

@pytest.mark.autorization
def test_login_tab_is_active_when_login_is_entered_in_the_field(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    # открываем страницу авторизации
    page.open()

    login = "rtkid_693043032823"
    # вводим логин в поле авторизации
    page.enter_login(login)
    # проверяем что таб Логин стал активным
    page.should_have_active_login_tab()

@pytest.mark.autorization
def test_account_tab_is_active_when_account_is_entered_in_the_field(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    # открываем страницу авторизации
    page.open()

    account_number = "166554362340"
    # вводим номер лицевого счета в поле авторизации
    page.enter_login(account_number)
    # проверяем что таб Лицевой счет стал активным
    page.should_have_active_account_tab()

@pytest.mark.autorization
def test_success_authorization_by_phone_number(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    # открываем страницу авторизации
    page.open()

    phone = "79171858489"
    password = "Psd34lKr"
    # вводим телефон в поле авторизации
    page.enter_phone(phone)
    # вводим пароль в поле авторизации
    page.enter_password(password)
    # нажимаем кнопку Войти
    page.click_enter_button()
    # проверяем что открылась страница личного кабинета
    page.should_have_opened_account_page()
    # выходим из аккаунта
    page.click_logout_button()

@pytest.mark.autorization
def test_success_authorization_by_email(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    # открываем страницу авторизации
    page.open()

    email = "midford0@gmail.com"
    password = "Psd34lKr"
    # вводим телефон в поле авторизации
    page.enter_email(email)
    # вводим пароль в поле авторизации
    page.enter_password(password)
    # нажимаем кнопку Войти
    page.click_enter_button()
    # проверяем что открылась страница личного кабинета
    page.should_have_opened_account_page()
    # выходим из аккаунта
    page.click_logout_button()

@pytest.mark.autorization
def test_success_authorization_by_account_number(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    # открываем страницу авторизации
    page.open()

    login = "rtkid_693043032823"
    password = "Psd34lKr"
    # вводим логин в поле авторизации
    page.enter_login(login)
    # вводим пароль в поле авторизации
    page.enter_password(password)
    # нажимаем кнопку Войти
    page.click_enter_button()
    # проверяем что открылась страница личного кабинета
    page.should_have_opened_account_page()
    # выходим из аккаунта
    page.click_logout_button()

@pytest.mark.autorization
def test_show_error_message_in_case_of_wrong_phone_or_password(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    # открываем страницу авторизации
    page.open()

    phone = "79171858489"
    password = "fdf3ewr"
    # вводим телефон в поле авторизации
    page.enter_phone(phone)
    # вводим неверный пароль в поле авторизации
    page.enter_password(password)
    # нажимаем кнопку Войти
    page.click_enter_button()
    # проверяем что появилась надпись "Неверный логин или пароль, и ссылка "Забыл пароль" окрасилпсь в красный цвет"
    page.should_have_error_message()

@pytest.mark.autorization
def test_show_error_message_in_case_of_wrong_email_or_password(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    # открываем страницу авторизации
    page.open()

    email = "midford0@gmail.com"
    password = "fdf3ewr"
    # вводим имеил в поле авторизации
    page.enter_email(email)
    # вводим неверный пароль в поле авторизации
    page.enter_password(password)
    # нажимаем кнопку Войти
    page.click_enter_button()
    # проверяем что появилась надпись "Неверный логин или пароль, и ссылка "Забыл пароль" окрасилпсь в красный цвет"
    page.should_have_error_message()

@pytest.mark.autorization
def test_show_error_message_in_case_of_wrong_login_or_password(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    # открываем страницу авторизации
    page.open()

    login = "rtkid_693043032823"
    password = "fdf3ewr"
    # вводим логин в поле авторизации
    page.enter_login(login)
    # вводим неверный пароль в поле авторизации
    page.enter_password(password)
    # нажимаем кнопку Войти
    page.click_enter_button()
    # проверяем что появилась надпись "Неверный логин или пароль", и ссылка "Забыл пароль" окрасилпсь в красный цвет
    page.should_have_error_message()

@pytest.mark.autorization
def test_recovery_password_page_opens(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Забыл пароль
    page.click_forgot_password_button()
    page2 = PasswordRecoveryPage(browser, browser.current_url)
    # проверяем, что открылась страница восстановления пароля
    page2.should_be_password_recovery_page()

@pytest.mark.autorization
def test_that_telephone_email_login_account_tabs_presented_on_recovey_password_page(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Забыл пароль
    page.click_forgot_password_button()
    page2 = PasswordRecoveryPage(browser, browser.current_url)
    # проверяем что на странице присутствуют табы телефон, имеил, логин, лицевой счет
    page2.should_have_tabs()
    # проверяем что таб Телефон выбран по умолчанию
    page2.should_have_active_telephone_tab()

@pytest.mark.autorization
def test_that_recovey_password_page_has_login_form(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Забыл пароль
    page.click_forgot_password_button()
    page2 = PasswordRecoveryPage(browser, browser.current_url)
    # проверяем, что есть форма для ввода данных
    page2.should_be_login_form()

@pytest.mark.autorization
def test_that_recovey_password_page_has_continue_button(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Забыл пароль
    page.click_forgot_password_button()
    page2 = PasswordRecoveryPage(browser, browser.current_url)
    # проверяем, что есть кнопка Продолжить
    page2.should_be_continue_button()

@pytest.mark.autorization
def test_that_recovey_password_page_has_back_button(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Забыл пароль
    page.click_forgot_password_button()
    page2 = PasswordRecoveryPage(browser, browser.current_url)
    # проверяем, что есть кнопка Продолжить
    page2.should_be_back_button()
