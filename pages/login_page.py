
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from pages.base_page import Base_page
from selenium.webdriver.support import expected_conditions as EC

class Login_page(Base_page):
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "pizokel_customer_submit")
    FORGOT_PASSWORD_LINK = (By.ID, "forget-password-open" )
    LOGIN_ERROR_MESSAGE = (By.CLASS_NAME, "error-message")


    def navigate_to_login_page(self):
        self.driver.get("https://www.fashiondays.ro/customer/authentication")


    def insert_email(self, email):
        self.driver.find_element(*self.EMAIL).send_keys(email)

    def insert_password(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)


    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def click_forgot_password_link(self):
        self.driver.find_element(*self.FORGOT_PASSWORD_LINK).click()

    def check_login_error_message(self,expected_message):
        try:
            actual_message = self.driver.find_element(*self.LOGIN_ERROR_MESSAGE).text
        except NoSuchElementException:
            actual_message = "None" # nu s-a afisat elementul
        EC.text_to_be_present_in_element((By.CLASS_NAME, "error-message"), expected_message)

    def verify_page_url(self):
        self.verify_page_url= 'https://www.fashiondays.ro/?tagName=women'



