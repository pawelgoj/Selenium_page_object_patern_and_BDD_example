import pytest
from utils.driver_factory import DriverFactory
from pages.home_page import HomePage


# Fixtures for login tests
@pytest.fixture()
def setup_chrome_tests(request):
    driver = DriverFactory.get_driver("chrome")
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield

    driver.quit()


@pytest.fixture()
def setup_firefox_tests(request):
    driver = DriverFactory.get_driver("firefox")
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield

    driver.quit()


# Fixtures for by item test
@pytest.fixture()
def precondition_logged_user_using_chrome(request):
    driver = DriverFactory.get_driver("chrome")
    driver.implicitly_wait(30)
    driver = log_in(driver)
    request.cls.driver = driver
    yield

    driver.quit()


@pytest.fixture()
def precondition_logged_user_using_firefox(request):
    driver = DriverFactory.get_driver("firefox")
    driver.implicitly_wait(30)
    driver = log_in(driver)
    request.cls.driver = driver
    yield

    driver.quit()


def log_in(driver):
    driver.get("https://www.saucedemo.com/")
    home_page = HomePage(driver)
    home_page.enter_username('standard_user')
    home_page.enter_password("secret_sauce")
    home_page.click_button()
    return driver
