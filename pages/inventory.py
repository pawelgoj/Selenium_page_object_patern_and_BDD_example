from ..locators.locators import InventoryLocators
import allure
import logging


class Inventory:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    @allure.step("Click <Add to cart> button of first item")
    def click_add_to_card_button_of_first_item(self) -> None:
        self.logger.info('clicking button <Add to cart>')
        button = self.driver.find_element(
            *InventoryLocators.button_of_first_item)
        if "Add to cart" in button.text:
            self.driver.click()

    @allure.step("Check <Remove> button is present")
    def check_remove_button_is_present(self) -> bool:
        self.logger.info('Check button <Remove> is present')
        button = self.driver.find_element(
            *InventoryLocators.button_of_first_item)
        if "Remove" in button.text:
            return True
        else:
            return False

    @allure.step("Check <Add to cart> button is present")
    def check_add_to_cart_button_is_present(self) -> bool:
        self.logger.info('Check button <Add to cart> is present')
        button = self.driver.find_element(
            *InventoryLocators.button_of_first_item)
        if "Add to cart" in button.text:
            return True
        else:
            return False

    @allure.step("Click <Remove> button of first item")
    def click_remove_button_of_first_item(self) -> None:
        self.logger.info('clicking button <Remove>')
        button = self.driver.find_element(
            *InventoryLocators.button_of_first_item)
        if "Remove" in button.text:
            self.driver.click()

    @allure.step("Click <shopping_cart_link> button")
    def click_shopping_cart_link_button(self) -> None:
        self.logger.info('clicking button <shopping_cart_link>')
        self.driver.find_element(
            *InventoryLocators.shopping_cart).click()

    @allure.step("Show all items")
    def show_all_items(self) -> None:
        self.logger.info('Show all items')
        self.driver.find_element(
            *InventoryLocators.menu_button).click()
        self.driver.find_element(
            *InventoryLocators.logout_button).click()

    @allure.step("Show about")
    def show_about(self) -> None:
        self.logger.info('Show about')
        self.driver.find_element(
            *InventoryLocators.menu_button).click()
        self.driver.find_element(
            *InventoryLocators.button_about).click()

    @allure.step("Logout")
    def logout(self) -> None:
        self.logger.info('Logout')
        self.driver.find_element(
            *InventoryLocators.menu_button).click()
        self.driver.find_element(
            *InventoryLocators.logout_button).click()

    @allure.step("Sort items a to z")
    def sort_items_A_to_Z(self):
        self.logger.info('Sort items a to z')
        self.driver.find_element(
            *InventoryLocators.menu_select_sort_method).click()
        self.driver.find_element(
            *InventoryLocators.button_sort_A_to_Z).click()

    @allure.step("Sort items z to a")
    def sort_items_Z_to_A(self):
        self.logger.info('Sort items z to a')
        self.driver.find_element(
            *InventoryLocators.menu_select_sort_method).click()
        self.driver.find_element(
            *InventoryLocators.button_sort_Z_to_A).click()

    @allure.step("Sort price low to high")
    def sort_price_low_to_high(self):
        self.logger.info('Sort price low to high')
        self.driver.find_element(
            *InventoryLocators.menu_select_sort_method).click()
        self.driver.find_element(
            *InventoryLocators.button_sort_low_to_high).click()

    @allure.step("Sort price high to low")
    def sort_price_high_to_low(self):
        self.logger.info('Sort price high to low')
        self.driver.find_element(
            *InventoryLocators.menu_select_sort_method).click()
        self.driver.find_element(
            *InventoryLocators.button_sort_high_to_low).click()

    @allure.step("Check items are sorted a to z")
    def check_items_are_sorted_a_to_z(self, nr_item_to_check: int) -> bool:
        self.logger.info('Check items are sorted a to z')

        previous_title = None
        for i in range(1, nr_item_to_check + 1):

            if previous_title is not None:
                word_1 = self.driver.find_element(
                    *InventoryLocators.get_locator_of_title_item(i)).text
            else:
                word_2 = self.driver.find_element(
                    *InventoryLocators.get_locator_of_title_item(i)).text

                if not Inventory._is_in_alphabetical_order(word_1, word_2):
                    return False

                word_1 = word_2

        return True

    @allure.step("Check items are sorted z to a")
    def check_items_are_sorted_z_to_a(self, nr_item_to_check: int) -> bool:
        self.logger.info('Check items are sorted z to a')
        previous_title = None
        for i in range(1, nr_item_to_check + 1):

            if previous_title is not None:
                word_1 = self.driver.find_element(
                    *InventoryLocators.get_locator_of_title_item(i)).text
            else:
                word_2 = self.driver.find_element(
                    *InventoryLocators.get_locator_of_title_item(i)).text

                if not Inventory._is_in_alphabetical_order(word_2, word_1):
                    return False

                word_1 = word_2

        return True

    @allure.step("Check prices are sorted low to high")
    def check_prices_are_sorted_low_to_high(self, nr_item_to_check: int)\
            -> bool:
        self.logger.info('Check prices are sorted low to high')
        previous_number = None
        for i in range(1, nr_item_to_check + 1):

            if previous_number is not None:
                price_1 = self.driver.find_element(
                    *InventoryLocators.get_locator_of_price_item(i)).text
                price_1 = int(price_1.replace("$", ""))
            else:
                price_2 = self.driver.find_element(
                    *InventoryLocators.get_locator_of_price_item(i)).text
                price_2 = int(price_1.replace("$", ""))
                if price_2 <= price_1:
                    return False

                price_1 = price_2

        return True

    @allure.step("Check prices are sorted high to low")
    def check_prices_are_sorted_high_to_low(self, nr_item_to_check: int)\
            -> bool:
        self.logger.info('Check prices are sorted high to low')
        previous_number = None
        for i in range(1, nr_item_to_check + 1):

            if previous_number is not None:
                price_1 = self.driver.find_element(
                    *InventoryLocators.get_locator_of_price_item(i)).text
                price_1 = int(price_1.replace("$", ""))
            else:
                price_2 = self.driver.find_element(
                    *InventoryLocators.get_locator_of_price_item(i)).text
                price_2 = int(price_1.replace("$", ""))
                if price_2 >= price_1:
                    return False

                price_1 = price_2

        return True

    @ staticmethod
    def _is_in_alphabetical_order(word_1: str, word_2: str):
        if len(word_1) > len(word_2):
            number_of_characters_to_check = len(word_2)
        else:
            number_of_characters_to_check = len(word_1)

        for i in range(number_of_characters_to_check):
            if word_1[i] > word_2[i]:
                return False
        return True
