from selenium.webdriver.common.by import By


class HomePageLocators:

    input_username = (By.ID, "user-name")
    input_password = (By.ID, "password")
    button = (By.ID, "login-button")
    error_message = (By.CSS_SELECTOR, "div.error>h3")


class InventoryLocators:
    menu_button = (By.ID, "bm-burger-button")
    button_of_first_item = (By.XPATH, "//div[@class='inventory_list']/div[1]"
                            + "/div[2]/div[2]/button")
    menu_select_sort_method = (By.CSS_SELECTOR, ".product_sort_container")
    button_sort_A_to_Z = (By.CSS_SELECTOR, "[value=az]")
    button_sort_Z_to_A = (By.CSS_SELECTOR, "[value=za]")
    button_sort_low_to_high = (By.CSS_SELECTOR, "[value=lohi]")
    button_sort_high_to_low = (By.CSS_SELECTOR, "[value=hilo]")
    shopping_cart = (By.CSS_SELECTOR, ".shopping_cart_link")
    logout_button = (By.ID, "logout_sidebar_link")
    button_add_backpack_to_cart = (By.ID, "add-to-cart-sauce-labs-backpack")
    button_all_items = (By.ID, "inventory_sidebar_link")
    button_about = (By.ID, "about_sidebar_link")

    @ staticmethod
    def get_locator_of_title_item(nr: int) -> tuple:
        return (By.XPATH, f"//div[@class='inventory_list']/div[{nr}]/div[2]/div[1]/a")

    @ staticmethod
    def get_locator_of_price_item(nr: int) -> tuple:
        return (By.XPATH, f'//div[@class="inventory_list"]/div[{nr}]/div[2]/div[2]/div[@class="inventory_item_price"]')


class CartLocators:
    remove_item_button = (By.ID, "remove-sauce-labs-backpack")
    checkout_button = (By.ID, "checkout")
    continue_shopping_button = (By.ID, "continue-shopping")
    menu_button = (By.ID, "bm-burger-button")
    cart_list = (By.CSS_SELECTOR, ".cart_list")
