from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.base_page import Page
from selenium.webdriver.support.wait import WebDriverWait


class SettingsPage(Page):

    SETTINGS_BUTTON = (By.XPATH, '//div[@class="g-menu-text" and contains(text(), "Settings")]')
    MY_CLIENTS = (By.XPATH, '//div[@class="setting-text" and  contains(text(), "My clients")]')
    TAG_PROPERTIES = (By.XPATH, '//div[@class="tag-properties-block wrap"]')
    EXPECTED_URL = 'https://soft.reelly.io/my-fixations'
    EXPECTED_URLS = 'https://soft.reelly.io/settings'
    EXPECTED_URLSL = 'https://soft.reelly.io/secondary-listings'
    NNTEETAGS = (By.XPATH, '//div[@class="settings-block-menu"]')
    CONNECT_COMPANY = (By.XPATH, '//div[@class="get-free-period menu"][contains(text(), "Connect the company")]')
    SECONDARY_BUTTON = (By.XPATH, '//div[@class="g-menu-text" and contains(normalize-space(text()), "Secondary")]')
    FILTERS = (By.XPATH, '//div[@wized="openFiltersWindow"]')
    WANT_TO_SELL = (By.CSS_SELECTOR, '[wized="ListingTypeSell"]')
    APPLY_FILTER = (By.CSS_SELECTOR, '[wized="applyFilterButtonMLS"]')
    FOR_SALE_TAG = (By.CSS_SELECTOR, '[w-el-text="For sale"]')


    def click_settings(self):
        # self.find_element(*self.SETTINGS_BUTTON).click()
        try:
            element = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(self.SETTINGS_BUTTON)
            )
            element.click()
            print("Settings clicked")
        except TimeoutException:
            print("Settings NOT found")
            raise

    def click_my_clients(self):
        self.click(*self.MY_CLIENTS)


    def click_filters(self):
        self.click(*self.FILTERS)


    def click_secondary(self):
        self.click(*self.SECONDARY_BUTTON)


    def click_want_to_sell(self):
        self.click(*self.WANT_TO_SELL)


    def click_apply_filter(self):
        self.click(*self.APPLY_FILTER)


    def url_opened(self):
            self.verify_url(self.EXPECTED_URL)

    def secondary_url(self):
        try:
            self.verify_url(self.EXPECTED_URLSL)
            print("Secondary URL opened successfully")
            return True
        except Exception as e:
            print(f"Failed to open Secondary URL: {e}")
            raise


    def settings_url(self):
            self.verify_url(self.EXPECTED_URLS)


    def verify_7elements_exist(self):
            try:
                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_all_elements_located(self.TAG_PROPERTIES)
                )
                print("Elements found")
                assert True
            except TimeoutException:
                print("Elements NOT found")
                assert False


    def verify_19options_exist(self):
            try:
                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_all_elements_located(self.NNTEETAGS)
                )
                print("19 Elements found")
                assert True
            except TimeoutException:
                print("19 Elements NOT found")
                assert False

    def verify_connect_company(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located(self.CONNECT_COMPANY)
            )
            print("Connection button found")
            assert True
        except TimeoutException:
            print("Connection button NOT found")
            assert False


    def verify_for_sale_tag(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located(self.FOR_SALE_TAG)
            )
            print("Tags found")
        except TimeoutException:
            print("Tags NOT found")
            assert False
