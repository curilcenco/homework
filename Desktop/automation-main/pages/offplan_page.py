from selenium.common import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import Page
from support.logger import logger


class OffPlan(Page):
    OFF_PLAN = (By.CSS_SELECTOR, "a[wized='newOffPlanLink']")

    def click_offplan(self):
        self.safe_click(*self.OFF_PLAN)
