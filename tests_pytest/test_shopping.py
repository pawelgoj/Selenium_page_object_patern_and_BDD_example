import allure
import pytest
import re
from pages.inventory import Inventory
from pages.cart import Cart
from pages.checkout_step_one import CheckoutStepOne
from pages.checkout_step_two import CheckoutStepTwo
from pages.checkout_complete import CheckoutComplete
from allure_commons.types import AttachmentType


class TestShopping:
    """Tests on two environments"""
    tax_percent: float = 8
    inventory_page = "https://www.saucedemo.com/inventory.html"
    checkout_step_two_page = "https://www.saucedemo.com/checkout-step-two.html"
    checkout_complete_page = "https://www.saucedemo.com/checkout-complete.html"
    cart_page = "https://www.saucedemo.com/cart.html"

    @ allure.title("Test add items to cart")
    @ allure.severity(allure.severity_level.CRITICAL)
    @ pytest.mark.parametrize("setup",
                              [
                                  "precondition_logged_user_using_chrome",
                                  "precondition_logged_user_using_firefox"
                              ])
    def test_add_items_to_cart(self,
                               setup, request,
                               number_of_products=3):
        request.getfixturevalue(setup)
        inventory = Inventory(self.driver)
        values_to_check = []
        for item in range(1, number_of_products + 1):
            title, price = inventory.click_add_to_card_button(item)
            values_to_check.append((title, price, "1"))

        inventory.click_shopping_cart_link_button()
        self.values_to_check = values_to_check
        self.cart = Cart(self.driver)
        assert self.cart.check_items_in_cart(values_to_check)

    @ allure.title("Test check buttons change text from <Add to cart> to <Remove>")
    @ allure.severity(allure.severity_level.MINOR)
    @ pytest.mark.parametrize("setup",
                              [
                                  "precondition_logged_user_using_chrome",
                                  "precondition_logged_user_using_firefox"
                              ])
    def test_check_change_buttons_state(self,
                                        setup, request,
                                        number_of_products=3):
        request.getfixturevalue(setup)
        inventory = Inventory(self.driver)

        checks = []
        for item in range(1, number_of_products + 1):
            inventory.click_add_to_card_button(item)
            checks.append(inventory.check_remove_button_is_present(item))
        self.driver.save_screenshot('screenie.png')
        assert all(checks)

    @ allure.title("Remove one item in cart")
    @ allure.severity(allure.severity_level.NORMAL)
    @ pytest.mark.parametrize("setup",
                              [
                                  "precondition_logged_user_using_chrome",
                                  "precondition_logged_user_using_firefox"
                              ])
    def test_remove_one_item_in_cart(self,
                                     setup, request):

        request.getfixturevalue(setup)
        self.test_add_items_to_cart(
            setup, request, number_of_products=3)
        self.cart.remove_item_from_cart(self.values_to_check[0][0])
        assert self.cart.check_item_is_removed(self.values_to_check[0][0])

    @ allure.title("Fill form correct data in checkout")
    @ allure.severity(allure.severity_level.CRITICAL)
    @ pytest.mark.parametrize("setup",
                              [
                                  "precondition_logged_user_using_chrome",
                                  "precondition_logged_user_using_firefox"
                              ])
    def test_fill_form_correct_data_in_checkout(self,
                                                setup, request):
        request.getfixturevalue(setup)
        self.test_add_items_to_cart(
            setup, request, number_of_products=3)
        self.cart.click_checkout()
        self.checkout_step_one = CheckoutStepOne(self.driver)
        self.checkout_step_one.fill_form("Tester", "Testowaty", "56-234")
        self.checkout_step_one.click_continue_button()
        assert self.checkout_step_two_page == self.driver.current_url

    @ allure.title("Fill form incorrect data in checkout")
    @ allure.severity(allure.severity_level.NORMAL)
    @ pytest.mark.parametrize("setup",
                              [
                                  "precondition_logged_user_using_chrome",
                                  "precondition_logged_user_using_firefox"
                              ])
    def test_fill_form_incorrect_data_in_checkout(self,
                                                  setup, request,
                                                  name, surname, zip, message):
        name = name.strip()
        surname = surname.strip()
        zip = zip.strip()

        request.getfixturevalue(setup)
        self.test_add_items_to_cart(
            setup, request, number_of_products=3)
        self.cart.click_checkout()
        self.checkout_step_one = CheckoutStepOne(self.driver)
        self.checkout_step_one.fill_form(name, surname, zip)
        self.checkout_step_one.click_continue_button()
        assert self.checkout_step_one.check_messagebox(message)

    @ allure.title("Check is correct data in checkout step two")
    @ allure.severity(allure.severity_level.CRITICAL)
    @ pytest.mark.parametrize("setup",
                              [
                                  "precondition_logged_user_using_chrome",
                                  "precondition_logged_user_using_firefox"
                              ])
    def test_check_is_correct_data_in_checkout_step_two(self,
                                                        setup, request):
        request.getfixturevalue(setup)
        self.test_fill_form_correct_data_in_checkout(
            setup, request)
        titles = [item[0] for item in self.values_to_check]
        self.checkout_step_two = CheckoutStepTwo(self.driver)

        assert self.checkout_step_two.check_products_in_checkout(titles)
        # Calculate sum of products
        sum_price = 0
        for item in self.values_to_check:
            mach = re.search('[0-9]+.[0-9]+', item[1])
            sum_price += float(mach[0])

        tax = round((self.tax_percent / 100) * sum_price, 2)
        sum_price = round(sum_price, 2)
        total = sum_price + tax

        checks = self.checkout_step_two.check_total_prices(sum_price,
                                                           tax, total)

        assert checks['total_price_without_tax']
        assert checks['tax']
        assert checks['total']

    @ allure.title("Finalize order")
    @ allure.severity(allure.severity_level.CRITICAL)
    @ pytest.mark.parametrize("setup",
                              [
                                  "precondition_logged_user_using_chrome",
                                  "precondition_logged_user_using_firefox"
                              ])
    def test_finalize_order(self, setup, request):
        request.getfixturevalue(setup)
        self.test_check_is_correct_data_in_checkout_step_two(
            setup, request
        )
        self.checkout_step_two.click_finish()
        self.checkout_complete = CheckoutComplete(self.driver)
        assert self.checkout_complete.check_message()\
            and self.checkout_complete_page == self.driver.current_url

    @ allure.title("From checkout-complete page back home")
    @ allure.severity(allure.severity_level.NORMAL)
    @ pytest.mark.parametrize("setup",
                              [
                                  "precondition_logged_user_using_chrome",
                                  "precondition_logged_user_using_firefox"
                              ])
    def test_from_checkout_complete_back_to_home(self,
                                                 setup, request):
        request.getfixturevalue(setup)
        self.test_finalize_order(setup, request)
        self.checkout_complete.click_back_to_home_button()
        assert self.inventory_page == self.driver.current_url

    @ allure.title("Show cart and then continue shopping")
    @ allure.severity(allure.severity_level.NORMAL)
    @ pytest.mark.parametrize("setup",
                              [
                                  "precondition_logged_user_using_chrome",
                                  "precondition_logged_user_using_firefox"
                              ])
    def test_show_cart_and_then_continue_shopping(self,
                                                  setup, request):
        request.getfixturevalue(setup)
        self.test_add_items_to_cart(
            setup, request, number_of_products=3)
        self.cart.click_continue_shopping()
        assert self.inventory_page == self.driver.current_url

    @ allure.title("Cancel filing checkout form")
    @ allure.severity(allure.severity_level.NORMAL)
    @ pytest.mark.parametrize("setup",
                              [
                                  "precondition_logged_user_using_chrome",
                                  "precondition_logged_user_using_firefox"
                              ])
    def test_cancel_filing_checkout_form(self,
                                         setup, request):
        request.getfixturevalue(setup)
        self.test_add_items_to_cart(
            setup, request, number_of_products=3)
        self.cart.click_checkout()
        self.checkout_step_one = CheckoutStepOne(self.driver)
        self.checkout_step_one.click_cancel_button()

        assert self.cart_page == self.driver.current_url

    @ allure.title("Sort items by price low to high")
    @ allure.severity(allure.severity_level.NORMAL)
    @ pytest.mark.parametrize("setup",
                              [
                                  "precondition_logged_user_using_chrome",
                                  "precondition_logged_user_using_firefox"
                              ])
    def test_sort_items_by_price_low_to_high(self,
                                             setup, request):
        request.getfixturevalue(setup)
        self.inventory = Inventory(self.driver)
        self.inventory.sort_price_low_to_high()

        allure.attach(self.driver.get_screenshot_as_png(),
                      name="test_sort_items_by_price_low_to_high",
                      attachment_type=AttachmentType.PNG)

        assert self.inventory.check_prices_are_sorted_by_price(4, 'asc')

    @ allure.title("Sort items by price high to low")
    @ allure.severity(allure.severity_level.NORMAL)
    @ pytest.mark.parametrize("setup",
                              [
                                  "precondition_logged_user_using_chrome",
                                  "precondition_logged_user_using_firefox"
                              ])
    def test_sort_items_by_price_high_to_low(self,
                                             setup, request):
        request.getfixturevalue(setup)
        self.inventory = Inventory(self.driver)
        self.inventory.sort_price_high_to_low()

        allure.attach(self.driver.get_screenshot_as_png(),
                      name="test_sort_items_by_price_high_to_low",
                      attachment_type=AttachmentType.PNG)

        assert self.inventory.check_prices_are_sorted_by_price(4, 'desc')

    @ allure.title("Sort items by name A to Z")
    @ allure.severity(allure.severity_level.NORMAL)
    @ pytest.mark.parametrize("setup",
                              [
                                  "precondition_logged_user_using_chrome",
                                  "precondition_logged_user_using_firefox"
                              ])
    def test_sort_items_by_name_a_to_z(self,
                                       setup, request):
        request.getfixturevalue(setup)
        self.inventory = Inventory(self.driver)
        self.inventory.sort_items_A_to_Z()

        allure.attach(self.driver.get_screenshot_as_png(),
                      name="test_sort_items_by_name_a_to_z",
                      attachment_type=AttachmentType.PNG)

        assert self.inventory.check_items_are_sorted_alphabetically(
            4, 'a_to_z')

    @ allure.title("Sort items by name Z to A")
    @ allure.severity(allure.severity_level.NORMAL)
    @ pytest.mark.parametrize("setup",
                              [
                                  "precondition_logged_user_using_chrome",
                                  "precondition_logged_user_using_firefox"
                              ])
    def test_sort_items_by_name_z_to_a(self,
                                       setup, request):
        request.getfixturevalue(setup)
        self.inventory = Inventory(self.driver)
        self.inventory.sort_items_Z_to_A()

        allure.attach(self.driver.get_screenshot_as_png(),
                      name="test_sort_items_by_name_z_to_a",
                      attachment_type=AttachmentType.PNG)

        assert self.inventory.check_items_are_sorted_alphabetically(
            4, 'z_to_a')
