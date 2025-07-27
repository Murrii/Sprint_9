from locators import recipe_card_page_locators as locators
from pages.base_page import BasePage
import allure


class RecipeCardPage(BasePage):
    @allure.step("Получаем текст названия рецепта")
    def get_title_text(self):
        return self.get_text_from_element(locators.RECIPE_NAME_LOCATOR)

    @allure.step("Проверяем, что отображается кнопка Добавить в список покупок")
    def is_add_to_shopping_list_button_visible(self):
        return self.is_element_visible(locators.ADD_TO_SHOPPING_LIST_BUTTON_LOCATOR)
