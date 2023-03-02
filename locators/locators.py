from selenium.webdriver.common.by import By


class HomePageLocators:

    input_username = (By.ID, "user-name")
    input_password = (By.ID, "password")
    button = (By.ID, "login-button")
    error_message = (By.CSS_SELECTOR, "div.error>h3")


class InventoryLocators:
    menu_button = (By.ID, "react-burger-menu-btn")
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

    # get locators related to items in order on page
    @ staticmethod
    def get_locator_of_button_of_item(nr: int) -> tuple:
        return (By.XPATH, f"//div[@class='inventory_list']/div[{nr}]/div[2]/div[2]/button")

    @ staticmethod
    def get_locator_of_title_of_item(nr: int) -> tuple:
        return (By.XPATH, f"//div[@class='inventory_list']/div[{nr}]/div[2]/div[1]/a/div")

    @ staticmethod
    def get_locator_of_price_of_item(nr: int) -> tuple:
        return (By.XPATH, f'//div[@class="inventory_list"]/div[{nr}]/div[2]/div[2]/div[@class="inventory_item_price"]')


class CartLocators:
    continue_shopping_button = (By.ID, "continue-shopping")
    checkout_button = (By.ID, "checkout")
    menu_button = (By.ID, "bm-burger-button")

    # Multiple cart items in list:
    cart_item = (By.CSS_SELECTOR, ".cart_item")
    # Locators for elements of item in list:
    remove_button = (By.TAG_NAME, "button")
    price = (By.CSS_SELECTOR, ".inventory_item_price")
    quantity = (By.CSS_SELECTOR, ".cart_quantity")
    title = (By.CSS_SELECTOR, ".inventory_item_name")


class CheckoutStepOneLocators:
    first_name_input = (By.ID, "first-name")
    last_name_input = (By.ID, "last-name")
    zip_input = (By.ID, "postal-code")
    cancel_button = (By.ID, "cancel")
    continue_button = (By.ID, "continue")
    message_box = (By.CSS_SELECTOR, ".error-message-container")


class CheckoutStepTwoLocators:
    # Multiple cart items in list:
    cart_item = (By.CSS_SELECTOR, ".cart_item")
    # Locators for elements of item in list:
    price = (By.CSS_SELECTOR, ".inventory_item_price")
    quantity = (By.CSS_SELECTOR, ".cart_quantity")
    title = (By.CSS_SELECTOR, ".inventory_item_name")
    total_price_without_tax = (By.CSS_SELECTOR, ".summary_subtotal_label")
    tax = (By.CSS_SELECTOR, ".summary_tax_label")
    total = (By.CSS_SELECTOR, ".summary_total_label")
    finish_button = (By.ID, "finish")
    cancel_button = (By.ID, "cancel")


class CheckoutCompleteLocators:
    message = (By.CSS_SELECTOR, ".complete-header")
    back_to_home_button = (By.ID, "back-to-products")
