import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from utilities.random_data_util import RandomDataUtil

#this is not playwright page, this is our own page created in conftest.py
def test_user_registration(page): 
    #page.goto() or page url will come from conftest.py
    home_page = HomePage(page)
    resgistration_page = RegistrationPage(page)

    home_page.click_my_account()
    home_page.click_register()

    random_data = RandomDataUtil()


    user_data = {
    "firstName": random_data.get_first_name(),
    "lastName": random_data.get_last_name(),
    "email": random_data.get_email(),
    "telephone": random_data.get_phone_number(),
    "password": random_data.get_password(),
}
   
    # first_name = random_data.get_first_name()
    # last_name = random_data.get_last_name()
    # email = random_data.get_email()
    # phone = random_data.get_phone_number()
    # password = random_data.get_password()
    

    # resgistration_page.set_first_name(first_name)
    # resgistration_page.set_last_name(last_name)
    # resgistration_page.set_email(email)
    # resgistration_page.set_telephone(phone)
    # resgistration_page.set_password(password)

    # resgistration_page.set_privacy_policy()
    # resgistration_page.click_continue()

    # confirmation_msg = resgistration_page.get_confirmation_msg()
    # expect(confirmation_msg).to_be_visible()

    #---Calling Complete resgistration-----------------

    resgistration_page.complete_registration(user_data)






