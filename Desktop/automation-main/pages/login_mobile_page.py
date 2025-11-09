# from time import sleep
#
# from selenium.common import TimeoutException
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from pages.base_page import Page
# from support.logger import logger
#
#
#
# class LoginMobilePage(Page):
#
#
#     # SEARCH_FILTER = (By.ID, "search-and-filters-button")
#     LOG_IN_BUTTON_B = (By.CSS_SELECTOR, 'a[wized="loginButton"]')
#     OFF_PLAN = (By.CSS_SELECTOR, 'div[class="menu-block"] a[wized="newOffPlanLink"]')
#     # EMAIL_INPUT = (By.ID, "email-2")
#     # PASSWORD_INPUT = (By.ID, "field")
#     # OVERLAY = "div.flex-row-center-2"
#     # SEARCH_FILTER = (By.CSS_SELECTOR, '[data-test-id="search-and-filters-button"]')
#     # OUT_OF_STOCK = (By.CSS_SELECTOR, '[data-test-id="filter-badge-out_of_stock"]')
#     # SHOW_PROJECTS = (By.CSS_SELECTOR, '[data-test-id="all-filters-submit"]')
#     # VERIFY_OUT_STOCK = (By.CSS_SELECTOR, 'span[data-test-id="project-card-sale-status"]')
#
#     def open_main_page(self):
#         self.driver.get('https://soft.reelly.io/sign-in')
#         sleep(5)
#
#
#     def enter_credentials(self):
#         self.input_text('i.curilcenco@gmail.com', *self.EMAIL_INPUT)
#         self.input_text('Zs.2bceN48Sy7z@', *self.PASSWORD_INPUT)
#
#
#     def click_login(self):
#         self.click(* self.LOG_IN_BUTTON_B)
#         sleep(5)
#
#
#     def input_email(self):
#         el = self.find_element(*self.EMAIL_INPUT)
#         el.clear()
#         el.send_keys('i.curilcenco@gmail.com')
#
#     def input_password(self):
#         self.find_element(*self.PASSWORD_INPUT).send_keys('Zs.2bceN48Sy7z@')
#
#
#     def search_filters(self, *locator):
#         self.wait.until(
#             EC.element_to_be_clickable(locator),
#             message=f'Element not clickable by {locator}'
#         ).click()
