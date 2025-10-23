from pages.base_page import Page
# from pages.cart_page import CartPage
# from pages.header import Header
# from pages.help_page import HelpPage
# from pages.main_page import MainPage
# from pages.search_results_page import SearchResultsPage
# from pages.target_app_page import TargetAppPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.base_page = Page(driver)