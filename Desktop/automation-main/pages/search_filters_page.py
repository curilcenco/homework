from selenium.common import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import Page
from support.logger import logger



class SearchFilters(Page):

    SEARCH_FILTER = (By.CSS_SELECTOR, 'button[data-test-id="search-and-filters-button"]')
    OUT_OF_STOCK = (By.CSS_SELECTOR, '[data-test-id="filter-badge-out_of_stock"]')
    SHOW_PROJECTS = (By.CSS_SELECTOR, '[data-test-id="all-filters-submit"]')
    VERIFY_OUT_STOCK = (By.CSS_SELECTOR, 'span[data-test-id="project-card-sale-status"]')

    def click_search_filters(self):
        self.click(*self.SEARCH_FILTER)

    def sales_status(self):
        self.wait_until_clickable_click(*self.OUT_OF_STOCK).click()

    def submit_projects(self):
        self.wait_until_clickable_click(*self.SHOW_PROJECTS)

    def verify_sales_status(self):
        self.verify_elements_exist(self.VERIFY_OUT_STOCK)