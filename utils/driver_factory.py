from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class DriverFactory:

    @staticmethod
    def get_driver(browser: str, selenium_grid_url: str | None = None):

        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            options.set_capability("browserName", "chrome")
            # options.set_capability("browserVersion", "110")
            options.set_capability("pageLoadStrategy", "eager")

            if selenium_grid_url is None:
                return webdriver.Chrome(service=ChromeService(
                    ChromeDriverManager().install()), options=options)
            else:
                return webdriver.Remote(selenium_grid_url, options=options)

        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            options.set_capability("browserName", "firefox")

            if selenium_grid_url is None:
                return webdriver.Firefox(service=FirefoxService(
                    GeckoDriverManager().install()), options=options)
            else:
                return webdriver.Remote(selenium_grid_url, options=options)

        else:
            raise Exception('Invalid driver name')
