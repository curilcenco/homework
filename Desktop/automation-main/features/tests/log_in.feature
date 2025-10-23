Feature: Test Scenarios for Search functionality


  Scenario: User can filter by Out of Stock
    Given the user opens the main page
    When the user clicks on "Log in"
    And enters valid credentials
    And clicks Log in
    And clicks on Off-plan
    Then Search and filters
    And selects the sales status Out of stock
    And clicks "Show projects"
    Then verify that only "Out of Stock" projects are displayed
