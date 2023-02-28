import pytest
from ..utils.driver_factory import DriverFactory

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





