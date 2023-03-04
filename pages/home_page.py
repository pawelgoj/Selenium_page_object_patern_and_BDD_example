from locators.locators import HomePageLocators
import allure
import logging
from allure_commons.types import AttachmentType


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    @allure.step("Enter username: '{1}'")
    def enter_username(self, username: str):
        self.logger.info(f'Entering username: {username}')
        input = self.driver.find_element(*HomePageLocators.input_username)
        input.click()
        input.send_keys(username)

    @allure.step("Enter password: '{1}'")
    def enter_password(self, password: str):
        self.logger.info(f'Entering password: {password}')
        input = self.driver.find_element(*HomePageLocators.input_password)
        input.click()
        input.send_keys(password)

    @allure.step("Click <LOGIN> button")
    def click_button(self):
        self.logger.info('clicking button <LOGIN>')
        self.driver.find_element(
            *HomePageLocators.button).click()

    @allure.step("Check message container '{1}'")
    def check_message_container_correct(self, message: str) -> bool:
        self.logger.info(f'Checking message: "{message}" in container')
        element = self.driver.find_element(*HomePageLocators.error_message)

        allure.attach(self.driver.get_screenshot_as_png(),
                      name="message_home_page",
                      attachment_type=AttachmentType.PNG)

        return element.get_attribute("textContent") == message
