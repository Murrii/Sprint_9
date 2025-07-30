from selenium.webdriver.common.by import By


EMAIL_TEXTFIELD_LOCATOR = (By.NAME, "email")
PASSWORD_TEXTFIELD_LOCATOR = (By.NAME, "password")
ENTER_ACCOUNT_BUTTON_LOCATOR = (By.TAG_NAME, "button")
PAGE_TITLE_LOCATOR = (By.TAG_NAME, "h1")
EXIT_BUTTON_LOCATOR = (By.XPATH, ".//*[text()='Выход']")