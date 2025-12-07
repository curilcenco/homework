from selenium.common import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from support.logger import logger

class Page:


    # LOG_IN_BUTTON_A = (By.ID, "signinButtonSignup")
    LOG_IN_BUTTON_B = (By.ID, "loginButton")
    EMAIL_INPUT = (By.ID, "email-2")
    PASSWORD_INPUT = (By.ID, "field")

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://soft.reelly.io'
        self.wait = WebDriverWait(self.driver, timeout=5)

    def open_url(self, url):
        logger.info(f'Opening url {url}')
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        logger.info(f'Clicking by {locator}...')
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        logger.info(f'Entering text {text} by {locator}...')
        self.driver.find_element(*locator).send_keys(text)

    def safe_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Element not clickable by {locator}").click()


    def continue_button(self):
        self.find_element(*self.LOG_IN_BUTTON_B).click()

    def send_text(self, locator, text):
        element = self.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def wait_until_clickable(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element not clickable by {locator}'
        )

    def wait_until_clickable_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element not clickable by {locator}'
        ).click()

    def wait_until_visible(self, *locator):
        self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element not visible by {locator}'
        )

    def wait_until_invisible(self, *locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f'Element still visible by {locator}'
        )

    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        print('Current windows ', all_windows)
        print('Switching to window: ', all_windows[1])
        self.driver.switch_to.window(all_windows[1])

    def switch_to_window_by_id(self, window_id):
        print('Switching to window: ', window_id)
        self.driver.switch_to.window(window_id)

    def hover_element(self, *locator):
        element = self.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()


    def click_field(self, locator):
        element = self.find_element(*locator)
        ActionChains(self.driver).move_to_element(element).click().perform()


    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text == actual_text, f'Expected text {expected_text} did not match actual {actual_text}'

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, f'Expected text {expected_text} not found in actual {actual_text}'

    def verify_url(self, expected_url):
        # current_url = self.driver.current_url
        # print(f'Current url {current_url}')
        # assert expected_url == current_url, f'Expected URL {expected_url}, but got {current_url}'
        self.wait.until(EC.url_to_be(expected_url), message=f'URL does not match {expected_url}')

    def verify_partial_url(self, expected_partial_url):
        # current_url = self.driver.current_url
        # print(f'Current url {current_url}')
        # assert expected_partial_url in current_url, f'Expected text {expected_partial_url} not in {current_url}'
        self.wait.until(EC.url_contains(expected_partial_url), message=f'URL does not contain {expected_partial_url}')


    def verify_elements_exist(self, locator, error_message=None):
        elements = self.driver.find_elements(*locator)
        assert len(elements) > 0, error_message or f"No elements found for {locator}"
        return elements


    def find_and_click(self, locator, timeout=10) :
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            # scroll by pixels
            self.driver.execute_script("""
                const yOffset = -120;
                const element = arguments[0];
                const y = element.getBoundingClientRect().top + window.pageYOffset + yOffset;
                window.scrollTo({top: y});
            """, element)

            try:
                element.click()
            except:
                self.driver.execute_script("arguments[0].click();", element)

            print(f"Successful click {locator}")

        except TimeoutException:
            print(f"Element {locator} not clickable {timeout} seconds")
        except Exception as e:
            print(f"No click was made {locator}: {e}")

    def find_click_mobile_local(self, locator):
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(locator)
            )
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});", element
            )
            self.driver.execute_script("arguments[0].click();", element)

            print("Out of Stock clicked")
            assert True
        except TimeoutException:
            print("Out of Stock NOT found")
            assert False

    def find_click_mobile(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
            )

            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            # #TouchActions
            # try:
            #     touch = TouchActions(self.driver)
            #     touch.tap(element).perform()
            # except Exception as e:
            #     # ActionChains
            #     actions = ActionChains(self.driver)
            #     actions.move_to_element(element).click().perform()
            #
            # print("Element clicked successfully")
            # assert True

        except TimeoutException:
            print("Element NOT found")
            assert False

    def close(self):
        self.driver.close()