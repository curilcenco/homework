from behave import given, when, then


@given('the user opens the main page emulation')
def main_page(context):
    context.app.login_page.open_main_page()


@when('enters valid email and password emulation')
def enter_credentials(context):
    context.app.login_page.enter_credentials()


@when('clicks Login emulation')
def button_login(context):
    context.app.login_page.click_login()


@when('clicks on Off-plan emulation')
def button_off_plan(context):
    print('pohhhh')
    context.app.offplan_page.click_offplan_mobile()


@then('Search and filters emulation')
def button_filters(context):
    context.app.search_filters_page.click_search_filters()


@then('selects the sales status Out of stock emulation')
def select_sales_status(context):

    context.app.search_filters_page.sales_status_mobile()



@then('clicks "Show projects" emulation')
def show_projects(context):
    context.app.search_filters_page.submit_projects()



@then('verify that only "Out of Stock" projects are displayed emulation')
def verify_out_of_stock(context):
    context.app.search_filters_page.verify_sales_status()
