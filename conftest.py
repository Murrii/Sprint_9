from selenium import webdriver
from pages.auth_page import AuthPage
from data import BASE_URL, REGISTER_URL, LOGIN_URL, CREATE_RECIPE_URL
from data import RECIPE_PIC_CATALOG
from pathlib import Path
import allure
import pytest
import string
import random


@pytest.fixture
@allure.title("генерируем данные для создания пользователя")
def generate_register_data():
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(3))
    register_data = "ktrof_" + random_string + "@yandex.ru"
    return register_data

@pytest.fixture
@allure.title("генерируем данные для валидного пароля")
def generate_password():
    letters = string.ascii_lowercase
    password = ''.join(random.choice(letters) for i in range(10))
    return password

@pytest.fixture
@allure.title("открываем страницу регистрации")
def driver_register_page():
    driver = webdriver.Chrome()
    driver.get(BASE_URL + REGISTER_URL)
    yield driver
    driver.quit()

@pytest.fixture
@allure.title("открываем страницу авторизации")
def driver_login_page():
    driver = webdriver.Chrome()
    driver.get(BASE_URL + LOGIN_URL)
    yield driver
    driver.quit()

@pytest.fixture
@allure.title("Авторизируемся и открываем страницу создания рецепта")
def driver_auth_create_recipe(driver_login_page):
    auth_page =  AuthPage(driver_login_page)
    auth_page.auth_with_walid_data()
    auth_page.is_auth_page_title_switch_to_main_page_title()
    driver_login_page.get(BASE_URL+CREATE_RECIPE_URL)
    yield driver_login_page

@pytest.fixture
@allure.title("Получаем файл из папки asserts")
def picture_path():
    path = Path(RECIPE_PIC_CATALOG)
    if path.exists():
        return str(path.absolute())
    else:
        pytest.skip(f"Test image {path} not found")