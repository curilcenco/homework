from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
from support.logger import logger

def create_firefox():
    options = FirefoxOptions()
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()
    logger.info("Local Firefox launched")
    return driver

def create_firefox_mobile():
    options = FirefoxOptions()
    options.set_preference(
        "general.useragent.override",
        "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) "
        "AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
    )

    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    driver.set_window_size(360, 640)
    logger.info("Local Firefox launched (360x640, Nexus 5 UA)")
    return driver