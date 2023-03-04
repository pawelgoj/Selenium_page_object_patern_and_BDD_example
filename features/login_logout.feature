@fixture.browser.firefox
Feature: Login and Logout


    Background:
        Given website "https://www.saucedemo.com/" is displayed


    Scenario: Login by correct data and logout
        When the user login by username "standard_user" and password "secret_sauce"
        Then website "https://www.saucedemo.com/inventory.html" is displayed
        When the user logout
        Then website "https://www.saucedemo.com/" is displayed


    Scenario: Locked user try login
        When the user login by username "locked_out_user" and password "secret_sauce"
        Then message "Epic sadface: Sorry, this user has been locked out." is displayed


    Scenario Outline: The user try login using wrong password or name
        When the user login by username: <name> and password: <password>
        Then message "Epic sadface: Username and password do not match any user in this service" is displayed

        Examples:
            | name            | password      |
            | Wrongname       | secret_sauce  |
            | standard_user   | 123fgrts      |
            | locked_out_user | '56843sdggsda |

