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



# By Xpath


# By Xpath, multiple attributes


# By Xpath, any tag


# By Xpath, using text


# partial text match