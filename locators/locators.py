from selenium.webdriver.common.by import By


class HomePageLocators:

    input_username = (By.ID, "user-name")
    input_password = (By.ID, "password")
    button = (By.ID, "login-button")
    error_message = (By.CSS_SELECTOR, "div.error>h3")


class InventoryLocators:
    menu_button = (By.ID, "bm-burger-button")
    list_of_items_to_by = (By.CSS_SELECTOR, ".inventory_list")
    select_container = (By.CSS_SELECTOR, ".select_container")
    shopping_cart = (By.CSS_SELECTOR, ".shopping_cart_link")
    logout_button = (By.ID, "logout_sidebar_link")
    button_add_backpack_to_cart = (By.ID, "add-to-cart-sauce-labs-backpack")


class Cart:
    remove_item_button = (By.ID, "remove-sauce-labs-backpack")
    checkout_button = (By.ID, "checkout")
    continue_shopping_button = (By.ID, "continue-shopping")
    menu_button = (By.ID, "bm-burger-button")
    cart_list = (By.CSS, ".cart_list")