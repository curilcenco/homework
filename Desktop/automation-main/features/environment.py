import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from app.application import Application
from support.logger import logger
import allure
import logging

logger = logging.getLogger(__name__)


def create_firefox_driver():

    mobile_emulation = {
        "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 1.2},
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) "
                     "AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19",
        "clientHints": {"platform": "Android", "mobile": True}
    }

    options = FirefoxOptions()
    options.set_preference("general.useragent.override", mobile_emulation["userAgent"])
    options.set_preference("layout.css.devPixelsPerPx", str(mobile_emulation["deviceMetrics"]["pixelRatio"]))
    options.set_preference("dom.w3c_touch_events.enabled", 1)

    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)

    driver.set_window_size(
        mobile_emulation["deviceMetrics"]["width"],
        mobile_emulation["deviceMetrics"]["height"]
    )

    logger.info("Local Firefox launched (360x640, Nexus 5 UA)")
    return driver


def create_browserstack_driver():
    USERNAME = os.getenv("BROWSERSTACK_USERNAME")
    ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")

    if not USERNAME or not ACCESS_KEY:
        raise Exception("BROWSERSTACK_USERNAME vs BROWSERSTACK_ACCESS_KEY")

    browserstack_url = f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

    options = FirefoxOptions()
    options.set_capability("browserName", "Firefox")
    options.set_capability("bstack:options", {
        "deviceName": "Samsung Galaxy S22",
        "realMobile": "true",
        "osVersion": "12.0",
        "projectName": "Mobile Tests",
        "buildName": "Mobile_Build_4",
        "sessionName": "Automation test on mobile",
        "seleniumVersion": "4.24.0"
    })

    return driver

def browser_init(context, scenario_name):
    run_mode = os.getenv("RUN_MODE", "local").lower()
    if run_mode == "browserstack":
        context.driver = create_browserstack_driver()
    else:
        context.driver = create_firefox_driver()

    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, timeout=10)
    context.app = Application(context.driver)
    logger.info(f"Start browser ({run_mode}) for scenario: {scenario_name}")


def before_scenario(context, scenario):
    print(f"\nStarted scenario: {scenario.name}")
    logger.info(f"\nStarted scenario: {scenario.name}")
    browser_init(context, scenario.name)


def before_step(context, step):
    print(f"\nStarted step: {step}")
    logger.info(f"Started step: {step}")


def after_step(context, step):
    if step.status == 'failed':
        print(f"\nStep failed: {step}")
        logger.warning(f"Step failed: {step}")

        screenshot_name = f"{step.name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
        screenshot_path = os.path.join("screenshots", screenshot_name)
        os.makedirs("screenshots", exist_ok=True)
        context.driver.save_screenshot(screenshot_path)

        allure.attach.file(
            screenshot_path,
            name=f"Screenshot_{step.name}",
            attachment_type=allure.attachment_type.PNG
        )


def after_scenario(context, scenario):
    if scenario.status == "failed":
        screenshot_name = f"{scenario.name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
        screenshot_path = os.path.join("screenshots", screenshot_name)
        os.makedirs("screenshots", exist_ok=True)
        context.driver.save_screenshot(screenshot_path)

        allure.attach.file(
            screenshot_path,
            name=f"Screenshot_{scenario.name}",
            attachment_type=allure.attachment_type.PNG
        )

    context.driver.quit()
    print(f"Browser closed for scenario: {scenario.name}")