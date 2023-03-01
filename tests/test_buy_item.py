from time import sleep
import allure
import pytest
from ..pages.inventory import Inventory
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions



class TestBuyItem:
    """Tests on two environments"""

    @ allure.title("Test buy firs item on website")
    @ pytest.mark.usefixture("precondition_logged_user_using_chrome")
    def test_add_items_to_cart(self,
                                      precondition_logged_user_using_chrome):
        inventory = Inventory(self.driver)
        inventory.click_add_to_card_button_of_first_item()

        sleep(100)
        assert False
