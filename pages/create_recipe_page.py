from locators import create_recipe_locators as locators
from pages.base_page import BasePage
from data import RECIPE_NAME, RECIPE_INGREDIENT_NAME, RECIPE_TIME, RECIPE_INGREDIENT_WEIGHT, RECIPE_DESCRIPTION
import allure


class CreateRecipePage(BasePage):
    @allure.step("Вводим название рецепта")
    def enter_recipe_name(self):
        self.fill_text_to_field(locators.RECIPE_NAME_FIELD_LOCATOR, RECIPE_NAME)

    @allure.step("Вводим название ингредиента")
    def enter_recipe_ingredient_name(self):
        self.fill_text_to_field(locators.INGREDIENT_NAME_FIELD_LOCATOR, RECIPE_INGREDIENT_NAME)
        self.click_on_element(locators.INGREDIENT_LIST_ITEM_LOCATOR)

    @allure.step("Вводим необходимое количество ингредиента")
    def enter_recipe_weight(self):
        self.fill_text_to_field(locators.INGREDIENT_WEIGHT_FIELD_LOCATOR, RECIPE_INGREDIENT_WEIGHT)

    @allure.step("Вводим время приготовления")
    def enter_recipe_time(self):
        self.fill_text_to_field(locators.TIME_FIELD_LOCATOR, RECIPE_TIME)

    @allure.step("Нажимаем на кнопку добавления рецепта")
    def click_on_add_ingredient_button(self):
        self.click_on_element(locators.INGREDIENT_ADD_BUTTON)

    @allure.step("Вводим описание рецепта")
    def enter_description(self):
        self.fill_text_to_field(locators.DESCRIPTION_FIELD_LOCATOR, RECIPE_DESCRIPTION)

    @allure.step("Загружаем картинку")
    def enter_picture(self, picture_path):
        self.load_picture(locators.LOAD_PICTURE_INPUT_LOCATOR, picture_path)

    @allure.step("Нажимаем на кнопку Создать рецепт")
    def click_on_create_recipe_button(self):
        self.move_page_down()
        self.click_on_element(locators.CREATE_RECIPE_BUTTON_LOCATOR)

    @allure.step("Создаем рецепт")
    def create_recipe(self, picture_path):
        self.enter_recipe_name()
        self.enter_recipe_ingredient_name()
        self.enter_recipe_weight()
        self.click_on_add_ingredient_button()
        self.enter_recipe_time()
        self.enter_description()
        self.enter_picture(picture_path)
        self.click_on_create_recipe_button()

