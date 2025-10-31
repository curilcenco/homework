from pages.base_page import Page
from pages.login_page import LoginPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.base_page = Page(driver)
        self.login_page = LoginPage(self.driver)