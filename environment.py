from browser import Browser
from pages.base_page import Base_page
from pages.forgot_password_page import ForgotPasswordPage
from pages.home_page import HomePage
from pages.login_page import Login_page



# before all o metoda care contine instructiuni ce trebuie executate inaintea tuturor testelor
def before_all(context):
    context.browser = Browser()
    context.login_page = Login_page()
    context.forgot_password_page = ForgotPasswordPage()
    context.base_page = Base_page()
    context.home_page = HomePage()

# context este o zona in care stochez toate obiectele instantiate in clasa in environment

# after all= metoda ce contine instructiuni ce trebuie efectuate dupa toate testele
def after_all(context):
    context.browser.close()


