import re
from behave import *
import allure
from allure_commons.types import AttachmentType
from pages.cart import Cart
from pages.checkout_complete import CheckoutComplete
from pages.checkout_step_one import CheckoutStepOne
from pages.checkout_step_two import CheckoutStepTwo

from pages.inventory import Inventory


@when(u'the user add "{quantity}" items to cart')
def user_add_items_to_cart(context, quantity):
    context.values_to_check = []
    for item in range(1, quantity + 1):
        title, price = context.inventory.click_add_to_card_button(item)
        context.values_to_check.append((title, price, "1"))


@when(u'click shopping cart link button')
def click_shopping_cart_link_button(context):
    context.inventory.click_shopping_cart_link_button()


@given(u'correct data in cart is displayed')
@then(u'correct data in cart is displayed')
def correct_data_in_cart_is_displayed(context):
    context.cart = Cart(context.driver)
    assert context.cart.check_items_in_cart(context.values_to_check)


@given(u'"{quantity}" items in cart')
def given_items_in_cart(context, quantity):
    context.values_to_check = []
    for item in range(1, quantity + 1):
        title, price = context.inventory.click_add_to_card_button(item)
        context.values_to_check.append((title, price, "1"))
    context.cart = Cart(context.driver)


@when(u'the user remove item from cart')
def user_remove_item_from_cart(context):
    context.cart.remove_item_from_cart(context.values_to_check[0][0])


@then(u'removed item is not present in cart')
def removed_item_is_not_present_in_cart(context):
    context.cart.check_item_is_removed(context.values_to_check[0][0])


@given(u'page "https://www.saucedemo.com/checkout-step-one.html" is displayed')
def page_is_displayed_step_one(context):
    allure.attach(context.driver.get_screenshot_as_png(),
                  name=f"step_one",
                  attachment_type=AttachmentType.PNG)
    context.cart.click_checkout()
    context.checkout_step_one = CheckoutStepOne(context.driver)


@when(u'the user fill form by: username: "{name}", surname: "{surname}" and zip: "{zip}"')
def the_user_fill_form_by(context, name, surname, zip):
    context.checkout_step_one.fill_form(name, surname, zip)
    context.checkout_step_one.click_continue_button()


@then(u'cart is displayed')
def cart_is_displayed(context):
    allure.attach(context.driver.get_screenshot_as_png(),
                  name="cart_page",
                  attachment_type=AttachmentType.PNG)

    assert context.driver.current_url == "https://www.saucedemo.com/cart.html"


@then(u'page "{web}" is displayed')
def then_page_is_displayed(context, web):
    allure.attach(context.driver.get_screenshot_as_png(),
                  name=f"{web}",
                  attachment_type=AttachmentType.PNG)

    assert context.driver.current_url == web


@then(u'correct data on page "https://www.saucedemo.com/checkout-step-two.html"')
def correct_data_on_page_checkout_step_two(context):

    titles = [item[0] for item in context.values_to_check]
    context.checkout_step_two = CheckoutStepTwo(context.driver)

    assert context.checkout_step_two.check_products_in_checkout(titles)
    # Calculate sum of products
    sum_price = 0
    for item in context.values_to_check:
        mach = re.search('[0-9]+.[0-9]+', item[1])
        sum_price += float(mach[0])

    tax = round((context.tax_percent / 100) * sum_price, 2)
    sum_price = round(sum_price, 2)
    total = sum_price + tax

    checks = context.checkout_step_two.check_total_prices(sum_price,
                                                          tax, total)

    assert checks['total_price_without_tax']
    assert checks['tax']
    assert checks['total']


@then(u'{message} is displayed')
def message_is_displayed_on_step_one(context, message):
    assert context.checkout_step_one.check_messagebox(message)


@when(u'the user click finish')
def the_user_click_finish(context):
    context.checkout_step_two.click_finish()


@then(u'correct message on page "https://www.saucedemo.com/checkout-complete.html"')
def correct_message_complete(context):
    context.checkout_complete = CheckoutComplete(context.driver)
    assert context.checkout_complete.check_message()


@when(u'the user click button back to home')
def the_user_click_button_back_to_home(context):
    context.checkout_complete.click_back_to_home_button()


@when(u'the user click continue button')
def the_user_click_continue_button(context):
    context.cart.click_continue_shopping()


@when(u'the user click button sort items low to high')
def the_user_click_button_sort_items_low_to_high(context):
    context.inventory.sort_price_low_to_high()
    assert context.inventory.check_prices_are_sorted_by_price(4, 'asc')


@then(u'items are sorted low to high')
def check_sort_items_low_to_high(context):
    assert context.inventory.check_prices_are_sorted_by_price(4, 'asc')


@when(u'the user click button sort items high to low')
def the_user_click_button_sort_items_high_to_low(context):
    context.inventory.sort_price_high_to_low()


@then(u'items are sorted high to low')
def check_sort_items_high_to_low(context):
    assert context.inventory.check_prices_are_sorted_by_price(4, 'desc')


@when(u'the user click button sort items A to Z')
def the_user_click_button_sort_items_A_to_Z(context):
    context.inventory.sort_items_A_to_Z()


@then(u'items are sorted A to Z')
def check_sort_items_A_to_Z(context):
    assert context.inventory.check_items_are_sorted_alphabetically(
        4, 'a_to_z')


@when(u'the user click button sort items Z to A')
def the_user_click_button_sort_items_Z_to_A(context):
    context.inventory.sort_items_Z_to_A()


@then(u'items are sorted Z to A')
def check_sort_items_Z_to_A(context):
    assert context.inventory.check_items_are_sorted_alphabetically(
        4, 'z_to_a')


@when(u'the user click button cancel')
def the_user_click_button_cancel(context):
    context.checkout_step_one.click_cancel_button()
