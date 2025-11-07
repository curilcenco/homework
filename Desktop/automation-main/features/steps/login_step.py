from behave import given, when, then
from selenium.webdriver.common.by import By
from pages.base_page import Page


@given('the user opens the main page')
def main_page(context):
    context.app.login_page.open_main_page()


@when('enters valid email and password')
def enter_credentials(context):
    context.app.login_page.enter_credentials()


@when('clicks Login')
def button_login(context):
    context.app.login_page.click_login()


@when('clicks on Off-plan')
def button_off_plan(context):
    context.app.offplan_page.click_offplan()
    print('start')

@then('Search and filters')
def button_filters(context):
    print('enter filters')
    context.app.login_page.enter_filters()
    context.app.search_filters_page.click_search_filters.click()


@then('selects the sales status Out of stock')
def select_sales_status(context):
    context.app.search_filters_page.sales_status()


@then('clicks "Show projects"')
def show_projects(context):
    context.app.search_filters_page.submit_projects()


@then('verify that only "Out of Stock" projects are displayed')
def verify_out_of_stock(context):
    context.app.search_filters_page.verify_sales_status()
