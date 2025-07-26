from selenium.webdriver.common.by import By


NAME_TEXTFIELD_LOCATOR = (By.NAME, "first_name")
SURNAME_TEXTFIELD_LOCATOR = (By.NAME, "last_name")
USERNAME_TEXTFIELD_LOCATOR = (By.NAME, "username")
EMAIL_TEXTFIELD_LOCATOR = (By.NAME, "email")
PASSWORD_TEXTFIELD_LOCATOR = (By.NAME, "password")
CREATE_ACCOUNT_BUTTON_LOCATOR = (By.TAG_NAME, "button")
HEADER_ENTER_BUTTON_LOCATOR = (By.XPATH, ".//*[@href='/signin']")