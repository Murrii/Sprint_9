from locators import auth_page_locators as locators
from pages.base_page import BasePage
from data import LOGIN_DATA_EMAIL, LOGIN_DATA_PASSWORD
from data import AUTH_TITLE_TEXT, MAIN_TITLE_TEXT
import allure


class AuthPage(BasePage):
    @allure.step("Вводим емейл")
    def enter_email(self):
        self.fill_text_to_field(locators.EMAIL_TEXTFIELD_LOCATOR, LOGIN_DATA_EMAIL)

    @allure.step("Вводим пароль")
    def enter_password(self):
        self.fill_text_to_field(locators.PASSWORD_TEXTFIELD_LOCATOR, LOGIN_DATA_PASSWORD)

    @allure.step("Нажимаем на кнопку Войти")
    def click_or_login_button(self):
        self.click_on_element(locators.ENTER_ACCOUNT_BUTTON_LOCATOR)

    @allure.step("Проверяем, что заголовок страницы авторизации поменялся на заголовок главной страницы")
    def is_auth_page_title_switch_to_main_page_title(self):
        self.wait_change_of_element(locators.PAGE_TITLE_LOCATOR, AUTH_TITLE_TEXT)
        new_text = self.get_text_from_element(locators.PAGE_TITLE_LOCATOR)
        return new_text == MAIN_TITLE_TEXT

    @allure.step("Проверяем видимость кнопки выхода")
    def is_exit_button_visible(self):
        return self.is_element_visible(locators.EXIT_BUTTON_LOCATOR)
