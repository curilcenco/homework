import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from app.application import Application
from support.logger import logger
import allure


def browser_init(context, scenario_name):
    run_mode = os.getenv("RUN_MODE", "local").lower()

    if run_mode == "browserstack":
        context.driver = create_browserstack_driver()
    else:
        context.driver = create_local_chrome()

    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, timeout=10)
    context.app = Application(context.driver)

    logger.info(f"Start browser ({run_mode}) for scenario: {scenario_name}")


# -----------------------------
# LOCAL CHROME
# -----------------------------
def create_local_chrome():
    options = ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )

    logger.info("Local Chrome launched")
    return driver


# -----------------------------
# BROWSERSTACK (CHROME)
# -----------------------------
def create_browserstack_driver():
    USERNAME = os.getenv("BROWSERSTACK_USERNAME")
    ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")

    if not USERNAME or not ACCESS_KEY:
        raise Exception("Missing BROWSERSTACK_USERNAME or BROWSERSTACK_ACCESS_KEY variables")

    browserstack_url = f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

    options = ChromeOptions()
    options.set_capability("browserName", "Chrome")
    options.set_capability("bstack:options", {
        "deviceName": "Samsung Galaxy S22",
        "realMobile": "true",
        "osVersion": "12.0",
        "projectName": "Mobile Tests",
        "buildName": "Mobile_Build_1",
        "sessionName": "Automation test on mobile",
        "seleniumVersion": "4.24.0"
    })

    driver = webdriver.Remote(
        command_executor=browserstack_url,
        options=options
    )

    logger.info("Remote BrowserStack Mobile Chrome (Samsung Galaxy S22)")
    return driver


# -----------------------------
# HOOKS
# -----------------------------
def before_scenario(context, scenario):
    print(f"\nStarted scenario: {scenario.name}")
    logger.info(f"Started scenario: {scenario.name}")
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

    if getattr(context, "driver", None):
        context.driver.quit()
        print(f"Browser closed for scenario: {scenario.name}")
        logger.info(f"Browser closed for scenario: {scenario.name}")