from pages.create_recipe_page import CreateRecipePage
from pages.recipe_card_page import RecipeCardPage
from data import RECIPE_NAME
import allure


class TestCreateRecipe:
    @allure.title("При создании рецепта осуществляется переход к карточке созданного рецепта")
    def test_create_recipe_jump_to_recipe_card_page(self, driver_auth_create_recipe, picture_path):
        page = CreateRecipePage(driver_auth_create_recipe)
        page.create_recipe(picture_path)
        recipe_card_page = RecipeCardPage(driver_auth_create_recipe)
        assert (recipe_card_page.is_add_to_shopping_list_button_visible() and
                recipe_card_page.get_title_text() == RECIPE_NAME)
