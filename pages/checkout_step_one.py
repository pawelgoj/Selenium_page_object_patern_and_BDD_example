from locators.locators import CheckoutStepOneLocators
from selenium.webdriver.common.action_chains import ActionChains
import allure
import logging


class CheckoutStepOne:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    @allure.step("Fill form")
    def fill_form(self, name: str, surname: str, zip: str) -> None:
        self.logger.info(
            f'Filling form Name: {name} surname: {surname} zip: {zip}')

        input = self.driver.find_element(
            *CheckoutStepOneLocators.first_name_input)
        ActionChains(self.driver)\
            .move_to_element(input)\
            .click()\
            .send_keys(name)\
            .perform()

        input = self.driver.find_element(
            *CheckoutStepOneLocators.last_name_input)
        ActionChains(self.driver)\
            .move_to_element(input)\
            .click()\
            .send_keys(surname)\
            .perform()

        input = self.driver.find_element(*CheckoutStepOneLocators.zip_input)
        ActionChains(self.driver)\
            .move_to_element(input)\
            .click()\
            .send_keys(zip)\
            .perform()

    @allure.step("Click <Continue> button")
    def click_continue_button(self) -> None:
        self.logger.info('clicking <Continue> button')
        self.driver.find_element(
            *CheckoutStepOneLocators.continue_button).click()

    @allure.step("Click <Cancel> button")
    def click_cancel_button(self) -> None:
        self.logger.info('clicking <Cancel> button')
        self.driver.find_element(
            *CheckoutStepOneLocators.cancel_button).click()

    @allure.step("Check messagebox")
    def check_messagebox(self, message: str) -> bool:
        text = self.driver.find_element(
            *CheckoutStepOneLocators.message_box
        ).text

        if message in text:
            return True
        else:
            return False
