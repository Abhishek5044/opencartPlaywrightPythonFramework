# import pytest
# from playwright.sync_api import expect
# from pages.home_page import HomePage
# from pages.registration_page import RegistrationPage
# from utilities.random_data_util import RandomDataUtil

# #this is not platwright page, this is our own page created in conftest.py
# def test_user_registration(page): 
#     #page.goto() or page url will come from conftest.py
#     home_page = HomePage(page)
#     resgistration_page = RegistrationPage(page)

#     home_page.click_my_account()
#     home_page.click_register()

#     random_data = RandomDataUtil()

#     first_name = random_data.get_first_name()
#     last_name = random_data.get_last_name()
#     email = random_data.get_email()
#     phone = random_data.get_phone_number()
#     password = random_data.get_password()

#     resgistration_page.set_first_name(first_name)
#     resgistration_page.set_last_name(last_name)
#     resgistration_page.set_email(email)
#     resgistration_page.set_telephone(phone)
#     resgistration_page.set_password(password)

#     resgistration_page.set_privacy_policy()
#     resgistration_page.click_continue()

#     confirmation_msg = resgistration_page.get_confirmation_msg()
#     expect(confirmation_msg).to_be_visible()

import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.registration_page import ResgisrationPage
from utilities.random_data_util import RandomDataUtil

@pytest.mark.sanity
def test_user_registration(page):
    home_page = HomePage(page)
    resgistration_page = ResgisrationPage(page)

    print(home_page.get_home_page_title())
    home_page.click_my_account_link()
    home_page.click_register_link()

    random_data = RandomDataUtil()

    first_name = random_data.get_first_name()
    last_name = random_data.get_last_name()
    email = random_data.get_email()
    password = random_data.get_password()
    phone = random_data.get_phone_number()

    resgistration_page.set_first_name(first_name)
    resgistration_page.set_last_name(last_name)
    resgistration_page.set_email(email)
    resgistration_page.set_password(password)
    resgistration_page.set_phone_number(phone)


    resgistration_page.check_privacy_policy()
    resgistration_page.click_continue_btton()

   

    conf_msg = resgistration_page.get_confirm_messgae()
    expect(conf_msg).to_have_text("Your Account Has Been Created!!")


