from pages.auth_page import AuthPage
import allure


class TestAuth:
    @allure.title("При успешной авторизации осуществляется переход на главную страницу")
    def test_register_with_all_valid_data_jump_to_auth_page(self, driver_login_page):
        auth_page = AuthPage(driver_login_page)
        auth_page.auth_with_walid_data()
        assert auth_page.is_auth_page_title_switch_to_main_page_title() and auth_page.is_exit_button_visible()
