from selenium import webdriver
from data import BASE_URL, REGISTER_URL
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
def driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL + REGISTER_URL)
    yield driver
    driver.quit()
