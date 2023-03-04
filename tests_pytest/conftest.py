import pytest
from utils.driver_factory import DriverFactory
from pages.home_page import HomePage
# pandas for importing and processing data from csv files (excel source)
import pandas as pd


# To generate parametrization from file
def pytest_generate_tests(metafunc):
    if "name" in metafunc.fixturenames\
            and "surname" in metafunc.fixturenames\
            and "zip" in metafunc.fixturenames\
            and "message" in metafunc.fixturenames:

        df = pd.read_csv(
            'data_for_tests/wrong_checkout_form_test_data.csv', sep=";")
        df = df.fillna("")

        data = [(df.loc[i]["name"], df.loc[i]["surname"], df.loc[i]["zip"],
                df.loc[i]["message"]) for i in range(df.shape[0])]

        metafunc.parametrize("name, surname, zip, message", data)


# Fixtures for login tests
@pytest.fixture()
def setup_chrome_tests(request):
    driver = DriverFactory.get_driver("chrome")
    driver.implicitly_wait(30)
    request.cls.driver = driver
    yield

    driver.quit()


@pytest.fixture()
def setup_firefox_tests(request):
    driver = DriverFactory.get_driver("firefox")
    driver.implicitly_wait(30)
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
