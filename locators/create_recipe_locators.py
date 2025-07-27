from selenium.webdriver.common.by import By


RECIPE_NAME_FIELD_LOCATOR = (By.XPATH, ".//div[text()='Название рецепта']/../input")
INGREDIENT_NAME_FIELD_LOCATOR = (By.XPATH, ".//div[text()='Ингредиенты']/../input")
INGREDIENT_LIST_ITEM_LOCATOR = (By.XPATH, ".//div[contains(@class, 'ingredientsInput')]/div[contains(@class, 'styles_container')]")
INGREDIENT_ADD_BUTTON = (By.XPATH, ".//div[text()='Добавить ингредиент']")
INGREDIENT_WEIGHT_FIELD_LOCATOR = (By.XPATH, ".//input[contains(@class, 'ingredientsAmountValue')]")
TIME_FIELD_LOCATOR = (By.XPATH, ".//div[text()='Время приготовления']/../input")
DESCRIPTION_FIELD_LOCATOR = (By.XPATH, ".//div[text()='Описание рецепта']/../textarea")
LOAD_PICTURE_INPUT_LOCATOR = (By.XPATH, ".//input[@type='file']")
CREATE_RECIPE_BUTTON_LOCATOR = (By.XPATH, ".//button[text()='Создать рецепт']")
