import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from config import Config
import time

def test_invalid_user_login(page):

    home_page = HomePage(page)
    logn_page = LoginPage(page)

    home_page.click_my_account()
    home_page.click_login()


    logn_page.set_email(Config.invalid_email)
    logn_page.set_login_password(Config.invalid_password)
    logn_page.click_login_button()

    time.sleep(3)
    error_msg = logn_page.get_login_error()
    expect(error_msg).to_be_visible(timeout=3000)

@pytest.mark.sanity
@pytest.mark.regression
def test_valid_user_login(page):

    home_page = HomePage(page)
    logn_page = LoginPage(page)
    my_accout_page = MyAccountPage(page)

    home_page.click_my_account()
    home_page.click_login()


    logn_page.set_email(Config.email)
    logn_page.set_login_password(Config.password)
    logn_page.click_login_button()

    title = my_accout_page.get_my_account_page_heading()
    expect(title).to_be_visible()
    