from pages.base_page import Page
from pages.login_page import LoginPage
from pages.offplan_page import OffPlan
from pages.search_filters_page import SearchFilters


class Application:


    def __init__(self, driver):
        self.driver = driver
        self.base_page = Page(driver)
        self.login_page = LoginPage(driver)
        self.offplan_page = OffPlan(driver)
        self.search_filters_page = SearchFilters(driver)

