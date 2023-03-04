from behave import *
import allure
from pages.home_page import HomePage
from pages.inventory import Inventory
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from allure_commons.types import AttachmentType


@given(u'website "{web}" is displayed')
def display_website(context, web):
    context.driver.get(web)
    context.home_page = HomePage(context.driver)


@when(u'the user login by username "{name}" and password "{password}"')
def login_correct_user(context, name, password):
    context.home_page.enter_username(name)
    context.home_page.enter_password(password)
    context.home_page.click_button()


@then(u'website "{web}" is displayed')
def check_website_is_displayed_inventory(context, web):
    context.inventory = Inventory(context.driver)
    allure.attach(context.driver.get_screenshot_as_png(),
                  name="login",
                  attachment_type=AttachmentType.PNG)

    assert context.driver.current_url == web


@when(u'the user logout')
def log_out_correct_user(context):
    context.inventory.logout()


@then(u'message "{message}" is displayed')
def check_message(context, message):
    allure.attach(context.driver.get_screenshot_as_png(),
                  name=f"Test {message}",
                  attachment_type=AttachmentType.PNG)
    context.home_page.check_message_container_correct(message)


@when(u'the user login by username: {name} and password: {password}')
def login_user_incorrect_data(context, name, password):
    context.home_page.enter_username(name)
    context.home_page.enter_password(password)
    context.home_page.click_button()
