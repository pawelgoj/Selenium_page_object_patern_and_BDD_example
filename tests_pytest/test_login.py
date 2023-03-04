import allure
import pytest
from pages.home_page import HomePage
from pages.inventory import Inventory
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from allure_commons.types import AttachmentType


class TestLogin:
    """Tests on two environments"""
    website = "https://www.saucedemo.com/"
    correct_password = "secret_sauce"

    @ allure.title("Test normal user login and and logout")
    @ allure.severity(allure.severity_level.CRITICAL)
    @ pytest.mark.parametrize("setup",
                              [
                                  "setup_chrome_tests",
                                  "setup_firefox_tests"
                              ])
    def test_positive_user_login_and_logout(self, setup, request):
        request.getfixturevalue(setup)
        self.driver.get(self.website)
        home_page = HomePage(self.driver)
        home_page.enter_username('standard_user')
        home_page.enter_password(self.correct_password)
        home_page.click_button()
        inventory = Inventory(self.driver)

        allure.attach(self.driver.get_screenshot_as_png(),
                      name="login",
                      attachment_type=AttachmentType.PNG)

        assert self.driver.current_url == self.website + "inventory.html"
        inventory.logout()

        allure.attach(self.driver.get_screenshot_as_png(),
                      name="logout",
                      attachment_type=AttachmentType.PNG)

        assert self.driver.current_url == self.website

    @ allure.title("Test locked user login")
    @ allure.severity(allure.severity_level.CRITICAL)
    @ pytest.mark.parametrize("setup",
                              [
                                  "setup_chrome_tests",
                                  "setup_firefox_tests"
                              ])
    def test_locked_user(self, setup, request):
        request.getfixturevalue(setup)
        self.driver.get(self.website)
        home_page = HomePage(self.driver)
        home_page.enter_username('locked_out_user')
        home_page.enter_password(self.correct_password)
        home_page.click_button()
        assert home_page.check_message_container_correct("Epic sadface: Sorry, this"
                                                         + " user has been locked out.")

    @ allure.title("Test user login wrong password.")
    @ allure.severity(allure.severity_level.CRITICAL)
    @ pytest.mark.parametrize("username, password",
                              [
                                  ('standard_user', '123fgrts'),
                                  ('locked_out_user', '56843sdggsda')
                              ])
    @ pytest.mark.parametrize("setup",
                              [
                                  "setup_chrome_tests",
                                  "setup_firefox_tests"
                              ])
    def test_user_login_wrong_password(self, setup, request, username, password):
        request.getfixturevalue(setup)
        self.driver.get(self.website)
        home_page = HomePage(self.driver)
        home_page.enter_username(username)
        home_page.enter_password(password)
        home_page.click_button()
        assert home_page.check_message_container_correct("Epic sadface: Username and password do"
                                                         + " not match any user in this service")
