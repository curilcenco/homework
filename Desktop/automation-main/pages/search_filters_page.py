from selenium.common import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import Page
from support.logger import logger
from time import sleep



class SearchFilters(Page):

    SEARCH_FILTER = (By.CSS_SELECTOR, '[data-test-id="search-and-filters-button"]')
    OUT_OF_STOCK = (By.CSS_SELECTOR, '[data-test-id="filter-badge-out_of_stock"]')
    SHOW_PROJECTS = (By.CSS_SELECTOR, '[data-test-id="all-filters-submit"]')
    VERIFY_OUT_STOCK = (By.CSS_SELECTOR, 'span[data-test-id="project-card-sale-status"]')


    def click_search_filters(self):
        sleep(15)
        self.click(*self.SEARCH_FILTER)
        sleep(15)

    def enter_filters(self):
        self.click(*self.SEARCH_FILTER)


    def sales_status(self):
        self.find_and_click(self.OUT_OF_STOCK)

    def sales_status_mobile(self):
        self.find_click_mobile(self.OUT_OF_STOCK)


    def submit_projects(self):
        self.click(*self.SHOW_PROJECTS)
        sleep(15)

    def verify_sales_status(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.VERIFY_OUT_STOCK)
            )
            print("Out of Stock found")
            assert True
        except TimeoutException:
            print("Out of Stock NOT found")
            assert False