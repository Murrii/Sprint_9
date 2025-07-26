from pages.auth_page import AuthPage
from pages.register_page import RegisterPage
import allure


class TestAuth:
    @allure.title("При успешной авторизации осуществляется переход на главную страницу")
    def test_register_with_all_valid_data_jump_to_auth_page(self, driver):
        reg_page = RegisterPage(driver)
        reg_page.click_on_header_enter_button()
        auth_page = AuthPage(driver)
        auth_page.enter_email()
        auth_page.enter_password()
        auth_page.click_or_login_button()
        assert auth_page.is_auth_page_title_switch_to_main_page_title() and auth_page.is_exit_button_visible()
