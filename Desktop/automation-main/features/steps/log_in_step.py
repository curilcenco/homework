from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
# from time import sleep

LOG_IN_BUTTON_A= (By.ID, "signinButtonSignup")
LOG_IN_BUTTON_B = (By.ID, "loginButton")
EMAIL_INPUT = (By.ID, "emailInput")
PASSWORD_INPUT = (By.ID, "passwordInput")
OFF_PLAN = (By.ID, "offPlanOld")
SEARCH_FILTERS = (By.ID, "search-and-filters-button")
OUT_OF_STOCK = (By.ID, "filter-badge-out_of_stock")
SHOW_PROJECTS = (By.ID, "all-filters-submit")
VERIFY_OUT_STOCK = (By.XPATH, "//div[contains(., 'Out Of Stock')]")



@given('the user opens the main page')
def main_page (context):
    context.app.base_page.open_url()

@when('the user clicks on "Log in"')
def login_page (context):
    context.app.base_page.wait_until_clickable_click(*LOG_IN_BUTTON_A)

@when('enters valid credentials')
def credentials (context):
    context.app.base_page.input_text(*EMAIL_INPUT, "i.curilcenco@gmail.com")
    context.app.base_page.input_text(*PASSWORD_INPUT, "Zs.2bceN48Sy7z@")

@when('clicks Log in')
def btt_login (context):
    context.app.base_page.click(*LOG_IN_BUTTON_B)

@when('clicks on Off-plan')
def btt_off_plan (context):
    context.app.base_page.wait_until_clickable_click(*OFF_PLAN)

@then('Search and filters')
def search_filters (context):
    context.app.base_page.wait_until_clickable_click(*SEARCH_FILTERS)

@then('selects the sales status Out of stock')
def select_sales_status (context):
    context.app.base_page.click(*OUT_OF_STOCK)

@then('clicks "Show projects"')
def show_projects (context):
    context.app.base_page.click(*SHOW_PROJECTS)

@then('verify that only "Out of Stock" projects are displayed')
def verify_out_of_stock(context):
    elements = context.app.base_page.find_elements(*VERIFY_OUT_STOCK)
    assert len(elements) > 0, "No 'Out Of Stock' projects found"