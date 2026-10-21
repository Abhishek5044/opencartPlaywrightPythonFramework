# registration_page.py
from playwright.sync_api import Page


class RegistrationPage:
    """
    Page Object Model class for the Registration Page.
    This class contains web element locators and methods (actions)
    to interact with the registration form.
    """

    def __init__(self, page: Page):
        self.page = page

        # ===== Locators =====
        # Input fields
        self.txt_firstname = page.locator('#input-firstname')
        self.txt_lastname = page.locator('#input-lastname')
        self.txt_email = page.locator('#input-email')
        self.txt_telephone = page.locator('#input-telephone')
        self.txt_password = page.locator('#input-password')
        self.txt_confirm_password = page.locator('#input-confirm')

        # Checkbox and buttons
        self.chk_policy = page.locator('input[name="agree"]')
        self.btn_continue = page.locator('input[value="Continue"]')

        # Confirmation message (displayed after successful registration)
        self.msg_confirmation = page.locator('div[id="content"] h1')

    # ===== Action Methods =====

    def set_first_name(self, fname: str):
        """Enter the user's first name into the 'First Name' field."""
        self.txt_firstname.fill(fname)

    def set_last_name(self, lname: str):
        """Enter the user's last name into the 'Last Name' field."""
        self.txt_lastname.fill(lname)

    def set_email(self, email: str):
        """Enter the user's email address."""
        self.txt_email.fill(email)

    def set_telephone(self, tel: str):
        """Enter the user's telephone number."""
        self.txt_telephone.fill(tel)

    def set_password(self, pwd: str):
        """Enter the password."""
        self.txt_password.fill(pwd)

    def set_confirm_password(self, pwd: str):
        """Re-enter the password in the 'Confirm Password' field."""
        self.txt_confirm_password.fill(pwd)

    def set_privacy_policy(self):
        """Select the 'Privacy Policy' checkbox."""
        self.chk_policy.check()

    def click_continue(self):
        """Click on the 'Continue' button to submit the registration form."""
        self.btn_continue.click()

    def get_confirmation_msg(self):
        """
        Return the confirmation message locator.
        This can be used to verify successful registration.
        """
        return self.msg_confirmation    #returnong message confirmation locator, not actual text

    # ===== Combined Workflow =====

    def complete_registration(self, user_data: dict):
        """
        Complete the full registration process using provided user data.

        Example:
        user_data = {
            "firstName": "John",
            "lastName": "Doe",
            "email": "john.doe@example.com",
            "telephone": "9876543210",
            "password": "Test@123"
        }
        """
        self.set_first_name(user_data["firstName"])
        self.set_last_name(user_data["lastName"])
        self.set_email(user_data["email"])
        self.set_telephone(user_data["telephone"])
        self.set_password(user_data["password"])
        self.set_confirm_password(user_data["password"])
        self.set_privacy_policy()
        self.click_continue()

        # Return confirmation message element for validation
        return self.msg_confirmation

#---------------------------------------------------------Repating above code , on my own-----------------------------------------------------------------------------------------
# from playwright.sync_api import Page

# class ResgisrationPage():

#     def __init__(self,page:Page):

#         self.page = page

#         self.first_name = page.locator('#input-firstname')
#         self.last_name = page.locator('#input-lastname')
#         self.email = page.locator('#input-email')
#         self.phone_number = page.locator('#input-telephone')
#         self.password = page.locator('#input-password')
#         self.confirm_password = page.locator('#input-confirm')
#         self.privacy_policey = page.locator('input[value="1"][name="agree"]')
#         self.continue_btton = page.locator('input[value="Continue"]')
#         self.confirmation_msg = page.locator('div[id="content"] h1')



#     def set_first_name(self,first_name):
#         try:
#             self.first_name.fill(first_name)
#         except Exception as e:
#             print(f"Exception while entering first name {first_name} : {e}")

        
#     def set_last_name(self,last_name):
#         try:
#             self.last_name.fill(last_name)
#         except Exception as e:
#             print(f"Exception while entering last name {last_name} : {e}")
        
#     def set_email(self,email):
#         try:
#             self.email.fill(email)
#         except Exception as e:
#             print(f"Exception while entering email {email} : {e}")
        
#     def set_phone_number(self,phone_number):
#         try:
#             self.phone_number.fill(phone_number)
#         except Exception as e:
#             print(f"Exception while entering phone_number {phone_number} : {e}")
        
#     def set_password(self,password):
#         try:
#             self.password.fill(password)
#         except Exception as e:
#             print(f"Exception while entering password {password} : {e}")
        
#     def set_confirm_password(self,confirm_password):
#         try:
#             self.confirm_password.fill(confirm_password)
#         except Exception as e:
#             print(f"Exception while entering confirm password {confirm_password} : {e}")

#     def check_privacy_policy(self):
#         try:
#             self.privacy_policey.check()
#         except Exception as e:
#             print(f"Exception while checking check_policy : {e}")

#     def click_continue_btton(self):
#         try:
#             self.continue_btton.click()

#         except Exception as e:
#             print(f"Exception while clicking continue btton : {e}")

        
#     def get_confirm_messgae(self):
#         try:
#             return self.confirmation_msg
#         except Exception as e:
#             print("Expection on meaage")
#             raise