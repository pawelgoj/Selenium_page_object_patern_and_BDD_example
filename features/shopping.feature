@fixture.browser.firefox
Feature: Shopping

    Background:
        Given website "https://www.saucedemo.com/" is displayed
        When the user login by username "standard_user" and password "secret_sauce"
        Then website "https://www.saucedemo.com/inventory.html" is displayed

    Scenario: Add items to cart
        When the user add "3" items to cart
        And click shopping cart link button
        Then correct data in cart is displayed

    Scenario: Remove items from cart
        Given "3" items in cart
        When the user remove item from cart
        Then removed item is not present in cart

    Scenario: Filing correct data in firs step of checkout
        Given "3" items in cart
        And page "https://www.saucedemo.com/checkout-step-one.html" is displayed
        When the user fill form by: username: "Tester", surname: "Testowaty" and zip: "56-234"
        Then page "https://www.saucedemo.com/checkout-step-two.html" is displayed
        And correct data on page "https://www.saucedemo.com/checkout-step-two.html"

    @data_from_file
    Scenario Outline: Filing incorrect data in firs step of checkout
        Given "3" items in cart
        And page "https://www.saucedemo.com/checkout-step-one.html" is displayed
        When the user fill form by: username: "<name>", surname: "<surname>" and zip: "<zip>"
        Then <message> is displayed

        Examples:
            | name | surname | zip | message |
            |  *   |   *     |  *  |   *     |

    Scenario: User finalize order
        Given "3" items in cart
        And page "https://www.saucedemo.com/checkout-step-one.html" is displayed
        And the user fill form by: username: "Tester", surname: "Testowaty" and zip: "56-234"
        When the user click finish
        Then page "https://www.saucedemo.com/checkout-complete.html" is displayed
        And correct message on page "https://www.saucedemo.com/checkout-complete.html"

    Scenario: Come back to home from checkout complete
        Given page "https://www.saucedemo.com/checkout-complete.html" is displayed
        And page "https://www.saucedemo.com/checkout-step-one.html" is displayed
        When the user click button back to home 
        Then page "https://www.saucedemo.com/inventory.html" is displayed

    Scenario: Show cart and continue shopping
        Given "3" items in cart
        And correct data in cart is displayed
        When the user click continue button
        Then page "https://www.saucedemo.com/inventory.html" is displayed

    Scenario: Cancel checkout step two
        Given "3" items in cart
        And page "https://www.saucedemo.com/checkout-step-one.html" is displayed
        When the user click button cancel
        Then cart is displayed

    Scenario: Short items by price low to high
        When the user click button sort items low to high
        Then items are sorted low to high

    Scenario: Short items by price high to low
        When the user click button sort items high to low
        Then items are sorted high to low

    Scenario: Short items by price A to Z
        When the user click button sort items A to Z
        Then items are sorted A to Z

    Scenario: Short items by price Z to A
        When the user click button sort items Z to A
        Then items are sorted Z to A

