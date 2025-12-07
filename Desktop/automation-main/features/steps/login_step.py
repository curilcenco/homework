from behave import given, when, then


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
    print('done')


@then('Search and filters')
def button_filters(context):
    context.app.search_filters_page.click_search_filters()


@then('selects the sales status Out of stock')
def select_sales_status(context):
    context.app.search_filters_page.sales_status()


@then('clicks "Show projects"')
def show_projects(context):
    context.app.search_filters_page.submit_projects()



@then('verify that only "Out of Stock" projects are displayed')
def verify_out_of_stock(context):
    context.app.search_filters_page.verify_sales_status()



@when('clicks on settings option')
def click_settings_option(context):
    context.app.settings_page.click_settings()


@then('click on the “My clients” option')
def click_my_clients(context):
    context.app.settings_page.click_my_clients()


@then('Verify the right page opens')
def verify_right_page(context):
    context.app.settings_page.url_opened()


@then('Verify that the page contains the 7 options')
def verify_7_options(context):
    context.app.settings_page.verify_7elements_exist()


@then('Verify the right page')
def verify_settings_page(context):
     context.app.settings_page.settings_url()


@then('Verify there are 19 options for the settings')
def verify_19(context):
    context.app.settings_page.verify_19options_exist()


@then('Verify the “connect the company” button is available')
def button_verify_company(context):
    context.app.settings_page.verify_connect_company()


@when('Click on the "Secondary" option in the left side menu')
def click_secondary_option(context):
    context.app.settings_page.click_secondary()


@then('Verify the right Secondary page')
def verify_secondary_url(context):
    context.app.settings_page.secondary_url()

@then('Click on Filters')
def filters(context):
    context.app.settings_page.click_filters()

@then('Filter the products by "want to sell"')
def filter_to_sell(context):
    context.app.settings_page.click_want_to_sell()


@then('Click on Apply Filter')
def apply_filter(context):
    context.app.settings_page.click_apply_filter()


@then('Verify all cards have a "for sale" tag')
def verify_tags_for_sales(context):
    context.app.settings_page.verify_for_sale_tag()
