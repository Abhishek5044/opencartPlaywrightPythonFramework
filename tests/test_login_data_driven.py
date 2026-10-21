import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
# from config import Config
from utilities.data_reader_util import read_json_data,read_csv_data,read_excel_data
import time

#Load/read the data from the testdata files

# csv_data = read_csv_data("testdata/logindata.csv")
excel_data = read_excel_data("testdata/logindata.xlsx")
# json_data = read_json_data("testdata/logindata.json")


@pytest.mark.parametrize("testName,email,password,expected",excel_data) #Column name should be same(testName,email,password,expected as in logindata.xlsx)
def test_login_data_driven(page,testName,email,password,expected):

    home_page = HomePage(page)
    logn_page = LoginPage(page)
    my_accout_page = MyAccountPage(page)

    home_page.click_my_account()
    home_page.click_login()


    # logn_page.set_email(Config.email)
    # logn_page.set_login_password(Config.password)
    # logn_page.click_login_btton()

    logn_page.login(email,password)  #This parameters can be valid or invalid
    time.sleep(3)

    if expected == "success":
        title = my_accout_page.get_my_account_page_heading()
        expect(title).to_be_visible(timeout=3000)
    else:
        error_msg = logn_page.get_login_error()
        expect(error_msg).to_be_visible(timeout=3000)
    
