from time import sleep
from selenium.common import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import Page
from support.logger import logger



class OffPlan(Page):
    OFF_PLAN = (By.CSS_SELECTOR, 'div[class="menu-block"] a[wized="newOffPlanLink"]')
    OFF_PLAN_MOBILE = (By.CSS_SELECTOR, 'div[class="menu-mobile hero-menu"] a[wized="newOffPlanLink"]')

    def click_offplan(self):
        self.click(*self.OFF_PLAN)

    def click_offplan_mobile(self):
        self.click(*self.OFF_PLAN_MOBILE)


