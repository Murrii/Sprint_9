from locators import registration_page_locators as locators
from pages.base_page import BasePage
from data import REGISTER_BUTTON_TEXT, AUTH_BUTTON_TEXT
import allure


class RegisterPage(BasePage):
    @allure.step("Вводим имя")
    def enter_name(self, name):
        self.fill_text_to_field(locators.NAME_TEXTFIELD_LOCATOR, name)

    @allure.step("Вводим фамилию")
    def enter_surname(self, surname):
        self.fill_text_to_field(locators.SURNAME_TEXTFIELD_LOCATOR, surname)

    @allure.step("Вводим имя пользователя")
    def enter_username(self, username):
        self.fill_text_to_field(locators.USERNAME_TEXTFIELD_LOCATOR, username)

    @allure.step("Вводим емейл")
    def enter_email(self, email):
        self.fill_text_to_field(locators.EMAIL_TEXTFIELD_LOCATOR, email)

    @allure.step("Вводим сложный пароль")
    def enter_password(self, password):
        self.fill_text_to_field(locators.PASSWORD_TEXTFIELD_LOCATOR, password)

    @allure.step("Заполняем все текстовые поля")
    def fill_all_fields(self, email, password):
        self.enter_name(email)
        self.enter_surname(email)
        self.enter_username(email)
        self.enter_email(email)
        self.enter_password(password)

    @allure.step("Нажимаем на кнопку Создать аккаунт")
    def click_or_register_button(self):
        self.click_on_element(locators.CREATE_ACCOUNT_BUTTON_LOCATOR)

    @allure.step("Проверяем, что форма регистрации поменялась на форму авторизации")
    def is_reg_button_switch_to_auth_button(self):
        self.wait_change_of_element(locators.CREATE_ACCOUNT_BUTTON_LOCATOR, REGISTER_BUTTON_TEXT)
        new_text = self.get_text_from_element(locators.CREATE_ACCOUNT_BUTTON_LOCATOR)
        return new_text == AUTH_BUTTON_TEXT
