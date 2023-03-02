from locators.locators import CheckoutStepTwoLocators
import allure
import logging
import re


class CheckoutStepTwo:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    @allure.step("Check products in checkout")
    def check_products_in_checkout(self, titles: list[str]) -> bool:
        """Check products in checkout

        Args:
            titles (list[str]): titles of products to check

        Returns:
            bool: True/False
        """
        self.logger.info('Checking products in checkout')
        cart_items = self.driver.find_elements(
            *CheckoutStepTwoLocators.cart_item)

        checks = []
        for item in cart_items:
            if item.find_element(*CheckoutStepTwoLocators.title).text in titles:
                checks.append(True)
            else:
                checks.append(False)

        return all(checks)

    @allure.step("Check total prices (total_price_without_tax: '{1}', tax: '{2}', total: '{3}')")
    def check_total_prices(self, total_price_without_tax: float,
                           tax: float, total: float) -> dict[str, bool]:
        """Check total prices.

        Args:
            total_price_without_tax (float): total price without tax
            tax (float): tax
            total (float): total pice with tax

        Returns:
            dict[str, bool]: key- "total_price_without_tax" or "tax" or "total"
        """
        self.logger.info('Checking total prices')

        checks = {}

        total_price_without_tax_web = self.driver.find_element(
            *CheckoutStepTwoLocators.total_price_without_tax
        ).text

        mach = re.search("[0-9]+.[0-9]+", total_price_without_tax_web)
        total_price_without_tax_web = float(mach[0])

        value = True if total_price_without_tax_web\
            == total_price_without_tax else False

        checks.update({"total_price_without_tax": value})

        tax_web = self.driver.find_element(
            *CheckoutStepTwoLocators.tax
        ).text

        mach = re.search("[0-9]+.[0-9]+", tax_web)
        tax_web = float(mach[0])

        value = True if tax_web == tax else False

        checks.update({"tax": value})

        total_web = self.driver.find_element(
            *CheckoutStepTwoLocators.total
        ).text

        mach = re.search("[0-9]+.[0-9]+", total_web)
        total_web = float(mach[0])

        value = True if tax_web == tax else False

        checks.update({"total": value})

        return checks

    @allure.step("Click <finish> button")
    def click_finish(self) -> None:
        self.logger.info('clicking <finish> button')
        self.driver.find_element(
            *CheckoutStepTwoLocators.finish_button).click()

    @allure.step("Click <cancel> button")
    def click_cancel(self) -> None:
        self.logger.info('clicking <cancel> button')
        self.driver.find_element(
            *CheckoutStepTwoLocators.cancel_button).click()
