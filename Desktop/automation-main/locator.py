from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://soft.reelly.io')

# By ID
driver.find_element(By.ID, 'signinButtonSignup')
# LOG_IN_BUTTON_A = (By.ID, "signinButtonSignup")
# LOG_IN_BUTTON_B = (By.ID, "loginButton")
# EMAIL_INPUT = (By.ID, "emailInput")
# PASSWORD_INPUT = (By.ID, "passwordInput")
# OFF_PLAN = (By.ID, "offPlanOld")
# SEARCH_FILTERS = (By.ID, "search-and-filters-button")
# OUT_OF_STOCK = (By.ID, "filter-badge-out_of_stock")
# SHOW_PROJECTS = (By.ID, "all-filters-submit")



# By Xpath
# EMAIL_INPUT = (By.XPATH, "//input[@wized='emailInput']")

# By Xpath, multiple attributes


# By Xpath, any tag


# By Xpath, using text
# VERIFY_OUT_STOCK = (By.XPATH, "//div[contains(., 'Out Of Stock')]")

# partial text match

