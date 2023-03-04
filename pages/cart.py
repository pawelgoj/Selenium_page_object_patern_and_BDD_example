from locators.locators import CartLocators
import allure
import logging
from allure_commons.types import AttachmentType


class Cart:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    @allure.step("Check items in cart")
    def check_items_in_cart(self, values_to_check: list[str, str, str])\
            -> bool:
        """Check items in cart are correct.

        Args:
            values_to_check (list[str, str, str]): List of values (title,
            price, quantity)

        Returns:
            bool: True/False
        """
        self.logger.info('checking items in cart')
        cart_items = self.driver.find_elements(
            *CartLocators.cart_item)

        allure.attach(self.driver.get_screenshot_as_png(),
                      name="items_in_cart",
                      attachment_type=AttachmentType.PNG)

        if len(values_to_check) != len(cart_items):
            logging.warning("Wrong number of items in cart!!!")
            return False

        return_value = True

        for count, item in enumerate(cart_items):
            title = item.find_element(*CartLocators.title).text

            found_title = False
            for to_check in values_to_check:
                if title == to_check[0]:
                    found_title = True
                    if to_check[2] not in item.find_element(
                            *CartLocators.quantity).text:
                        logging.warning(
                            f"Item {count + 1} have wrong quantity!!!")
                        return_value = False
                    if to_check[1] not in item.find_element(
                            *CartLocators.price).text:
                        logging.warning(
                            f"Item {count + 1} have wrong price!!!")
                        return_value = False

            if not found_title:
                logging.warning(
                    f"Item {count + 1} have wrong title!!!")
                return_value = False

        return return_value

    @allure.step("Remove item from cart")
    def remove_item_from_cart(self, title: str) -> None:
        """Remove some products from Cart.

        Args:
            number_of_products (int): Number of products to remove
            title (str): Title of product to remove

        """
        self.logger.info('removing item from cart')
        cart_items = self.driver.find_elements(*CartLocators.cart_item)
        for item in cart_items:
            if title in item.find_element(*CartLocators.title).text:
                print(item.find_element(*CartLocators.title).text)
                print(item.find_element(*CartLocators.title).text)
                item.find_element(*CartLocators.remove_button).click()
                break

    @allure.step("Check item is removed")
    def check_item_is_removed(self, title: str) -> bool:
        self.logger.info('checking item is removed')
        cart_items = self.driver.find_elements(*CartLocators.cart_item)

        allure.attach(self.driver.get_screenshot_as_png(),
                      name="items_in_cart_removed",
                      attachment_type=AttachmentType.PNG)

        for item in cart_items:
            if title in item.find_element(*CartLocators.title).text:
                return False
        return True

    @allure.step("Click <checkout> button")
    def click_checkout(self) -> None:
        self.logger.info('clicking checkout')
        self.driver.find_element(
            *CartLocators.checkout_button).click()

    @allure.step("Click <continue shopping> button")
    def click_continue_shopping(self) -> None:
        self.logger.info('clicking continue_shopping')
        self.driver.find_element(
            *CartLocators.continue_shopping_button).click()
