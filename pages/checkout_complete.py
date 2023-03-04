from locators.locators import CheckoutCompleteLocators
import allure
import logging
from allure_commons.types import AttachmentType


class CheckoutComplete:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    @allure.step("Check message")
    def check_message(self, message: str = "Thank you for your order!") -> bool:
        self.logger.info('Checking message')
        message_web = self.driver.find_element(
            *CheckoutCompleteLocators.message).text

        allure.attach(self.driver.get_screenshot_as_png(),
                      name="check_message_checkout_complete",
                      attachment_type=AttachmentType.PNG)

        if message in message_web:
            return True
        else:
            return False

    @allure.step("Click <back-to-products> button")
    def click_back_to_home_button(self) -> None:
        self.logger.info('Clicking <back-to-products> button')
        self.driver.find_element(
            *CheckoutCompleteLocators.back_to_home_button).click()
