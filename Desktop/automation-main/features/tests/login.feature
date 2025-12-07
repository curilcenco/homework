Feature: Test Scenarios for Search functionality

    Background:
    Given the user opens the main page
    When enters valid email and password
    And clicks Login

  Scenario: User can filter by Out of Stock
    When clicks on Off-plan
    Then Search and filters
    And selects the sales status Out of stock
    And clicks "Show projects"
    Then verify that only "Out of Stock" projects are displayed

  Scenario: Users can access Whatsapp and Telegram communities
    When clicks on settings option
    Then click on the “My clients” option
    And Verify the right page opens
    And Verify that the page contains the 7 options

  Scenario: User can go to settings and see the right number of UI elements
    When clicks on settings option
    Then Verify the right page
    And Verify there are 19 options for the settings
    And Verify the “connect the company” button is available


  Scenario:  User can filter the Secondary deals by “want to sell” option
    When Click on the "Secondary" option in the left side menu
    Then Verify the right Secondary page
    And Click on Filters
    And Filter the products by "want to sell"
    And Click on Apply Filter
    And Verify all cards have a "for sale" tag