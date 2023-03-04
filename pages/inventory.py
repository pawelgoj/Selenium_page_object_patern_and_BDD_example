from locators.locators import InventoryLocators
import allure
import logging
from allure_commons.types import AttachmentType


class Inventory:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    @allure.step("Click <Add to cart> button of item")
    def click_add_to_card_button(self, item: int) -> tuple[str, str] | None:
        """Click add to card button

        Args:
            item (int): Number of item in order on webpage.

        Returns:
            tuple(str, str) | None: (title, price)
        """
        self.logger.info('clicking button <Add to cart>')
        button = self.driver.find_element(
            *InventoryLocators.get_locator_of_button_of_item(item))
        to_return = None

        if "Add to cart" in button.text:
            button.click()
            title = self.driver.find_element(
                *InventoryLocators.get_locator_of_title_of_item(item)).text
            price = self.driver.find_element(
                *InventoryLocators.get_locator_of_price_of_item(item)).text

            to_return = (title, price)

        return to_return

    @allure.step("Check <Remove> button is present")
    def check_remove_button_is_present(self, item: int) -> bool:
        self.logger.info(f'Check button <Remove> of item {item} is present')
        button = self.driver.find_element(
            *InventoryLocators.get_locator_of_button_of_item(item))

        allure.attach(self.driver.get_screenshot_as_png(),
                      name="check_remove_button",
                      attachment_type=AttachmentType.PNG)

        if "Remove" in button.text:
            return True
        else:
            return False

    @allure.step("Check <Add to cart> button is present")
    def check_add_to_cart_button_is_present(self, item: int) -> bool:
        self.logger.info('Check button <Add to cart> is present')
        button = self.driver.find_element(
            *InventoryLocators.get_locator_of_button_of_item(item))

        allure.attach(self.driver.get_screenshot_as_png(),
                      name="check_add_to_cart_button",
                      attachment_type=AttachmentType.PNG)

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
    def check_items_are_sorted_alphabetically(self, nr_item_to_check: int,
                                              order: str) -> bool:
        """Check are items in correct order.

        Args:
            nr_item_to_check (int): Number of items to check.
            order (str): 'a_to_z' or 'z_to-a'

        Returns:
            bool: True/False
        """
        self.logger.info('Check items are sorted a to z')

        allure.attach(self.driver.get_screenshot_as_png(),
                      name=f"check_items_are_sorted_alphabetically_{order}",
                      attachment_type=AttachmentType.PNG)

        word_1 = None
        for i in range(1, nr_item_to_check + 1):
            if word_1 is None:
                word_1 = self.driver.find_element(
                    *InventoryLocators.get_locator_of_title_of_item(i)).text
            else:
                word_2 = self.driver.find_element(
                    *InventoryLocators.get_locator_of_title_of_item(i)).text

                if not Inventory._is_in_alphabetical_order(word_1, word_2)\
                        and order == 'a_to_z':
                    return False
                elif not Inventory._is_in_alphabetical_order(word_2, word_1)\
                        and order == 'z_to_a':
                    return False

                word_1 = word_2

        return True

    @allure.step("Check prices are sorted low to high")
    def check_prices_are_sorted_by_price(self, nr_item_to_check: int,
                                         order: str) -> bool:
        """Check are items in correct order.

        Args:
            nr_item_to_check (int): Number of items to check.
            order (str): 'asc' or 'desc'

        Returns:
            bool: True/False
        """
        self.logger.info('Check prices are sorted low to high')

        allure.attach(self.driver.get_screenshot_as_png(),
                      name=f"check_prices_are_sorted_by_price_{order}",
                      attachment_type=AttachmentType.PNG)

        previous_number = None
        for i in range(1, nr_item_to_check + 1):

            if previous_number is None:
                price_1 = self.driver.find_element(
                    *InventoryLocators.get_locator_of_price_of_item(i)).text
                price_1 = float(price_1.replace("$", ""))
            else:
                price_2 = self.driver.find_element(
                    *InventoryLocators.get_locator_of_price_of_item(i)).text
                price_2 = float(price_1.replace("$", ""))
                if price_2 <= price_1 and order == 'asc':
                    return False
                elif price_1 <= price_2 and order == 'desc':
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
            elif word_2[i] > word_1[i]:
                return True
            else:
                continue
