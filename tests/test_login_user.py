import allure
import pytest
from ..pages.home_page import HomePage


@pytest.mark.usefixtures("setup")
class TestHomePage:

    @allure.title("Test user login")
    def test_user_login(self, setup):
        self.driver.get("https://www.saucedemo.com/")
        home_page = HomePage(self.driver)
        home_page.enter_username("standard_user")
        home_page.enter_password("secret_sauce")
        home_page.click_button()
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html"
