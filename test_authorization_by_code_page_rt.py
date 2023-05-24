import pytest
from .pages.authorization_by_code_page_rt import AuthorizationByCodePage


# проверяем что страница авторизации по коду открывается
@pytest.mark.code
def test_can_open_authorization_by_code_page(browser):
    link = "https://my.rt.ru/"
    page = AuthorizationByCodePage(browser, link)
    # открываем страницу авторизации по коду
    page.open()
    # проверяем что открылась именно страница авторизации по коду
    page.should_be_opened_authorization_by_code_page()

# проверяем что происходит отправка кода при авторизации по коду через телефон
@pytest.mark.code
def test_that_code_send_when_telephone_number_entered(browser):
    link = "https://my.rt.ru/"
    page = AuthorizationByCodePage(browser, link)
    # открываем страницу авторизации по коду
    page.open()

    phone = "79171858489"
    page.enter_phone(phone)
    page.click_get_code_button()
    # проверка что после отправки кода появляется соответствующее сообщение
    page.should_have_message_that_code_was_sent()

# проверяем что происходит отправка кода при авторизации по коду через телефон
@pytest.mark.code
def test_that_code_send_when_email_entered(browser):
    link = "https://my.rt.ru/"
    page = AuthorizationByCodePage(browser, link)
    # открываем страницу авторизации по коду
    page.open()
    email = "midford0@gmail.com"
    page.enter_email(email)
    page.click_get_code_button()
    # проверка что после отправки кода появляется соответствующее сообщение
    page.should_have_message_that_code_was_sent()

# проверяем что на странице авторизации по коду присутствует логотип
@pytest.mark.code
def test_that_logo_is_presented(browser):
    link = "https://my.rt.ru/"
    page = AuthorizationByCodePage(browser, link)
    # открываем страницу авторизации по коду
    page.open()
    # проверяем что на странице есть лого
    page.should_have_logo()


