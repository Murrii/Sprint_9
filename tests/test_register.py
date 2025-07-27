from pages.register_page import RegisterPage
import allure


class TestRegister:
    @allure.title("При успешной регистрации осуществляется переход на страницу авторизации")
    def test_register_with_all_valid_data_jump_to_auth_page(self, driver_register_page,
                                                            generate_register_data, generate_password):
        page = RegisterPage(driver_register_page)
        page.fill_all_fields(email=generate_register_data, password=generate_password)
        page.click_or_register_button()
        assert page.is_reg_button_switch_to_auth_button()
