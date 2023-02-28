import allure
import pytest
from ..pages.home_page import HomePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestHomePage:
    """Tests on two environments"""
    website = "https://www.saucedemo.com/"
    correct_password = "secret_sauce"

    @ allure.title("Test normal user login and by product and logout")
    @ pytest.mark.parametrize("setup",
                              [
                                  "setup_chrome_tests",
                                  "setup_firefox_tests"
                              ])
    def test_positive_user_login_and_by_product_and_logout(self, setup, request):
        request.getfixturevalue(setup)
        self.driver.get(self.website)
        home_page = HomePage(self.driver)
        home_page.enter_username('standard_user')
        home_page.enter_password(self.correct_password)
        home_page.click_button()
        assert self.driver.current_url == self.website + "inventory.html"

    @ allure.title("Test locked user login")
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

    @ allure.title("Test problem user login")
    @ pytest.mark.parametrize("setup",
                              [
                                  "setup_chrome_tests",
                                  "setup_firefox_tests"
                              ])
    def test_problem_user(self, setup, request):
        request.getfixturevalue(setup)
        self.driver.get(self.website)
        home_page = HomePage(self.driver)
        home_page.enter_username('problem_user')
        home_page.enter_password(self.correct_password)
        home_page.click_button()
        assert self.driver.current_url == self.website + "inventory.html"\

    def test_performance_glitch_user(self, setup_chrome_tests):
        pass

    @ allure.title("Test wrong password.")
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
    def test_wrong_password(self, setup, request, username, password):
        request.getfixturevalue(setup)
        self.driver.get(self.website)
        home_page = HomePage(self.driver)
        home_page.enter_username(username)
        home_page.enter_password(password)
        home_page.click_button()
        assert home_page.check_message_container_correct("Epic sadface: Username and password do"
            + " not match any user in this service")


