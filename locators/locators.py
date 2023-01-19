from selenium.webdriver.common.by import By


class HomePageLocators:

    input_username = (By.ID, "user-name")
    input_password = (By.ID, "password")
    button = (By.ID, "login-button")
    error_message = (By.CSS_SELECTOR, "div.error>h3")


class InventoryLocators:
    # TODO
    pass
