Feature: Temporary Worker Feature

    @TemporaryWorkerScreen @Regression @Sanity
    Scenario: Add new temporary worker Screen
        Given Go to the Base url
        Then Verify user is on "Login" screen
        When User fills "Valid" form data on "login" screen
        Then Verify user is on "HomePage" screen
        Then User clicks "Temporary Worker" button on "Homepage" screen
        Then Scroll "Down" into view "Add New Temporary Worker" Section
        Then User clicks "Add Temporary Worker" button on "Temporary Worker" screen
        Then Verify user is on "Add Temporary Worker" screen

    @TemporaryWorkerMandatoryFields @Regression @Sanity
    Scenario: Verify temporary worker Mandatory Fields Screen
        Given Go to the "Base" url
        Then Verify user is on "Login" screen
        When User fills "Valid" form data on "login" screen
        Then Verify user is on "HomePage" screen
        Then User clicks "Temporary Worker" button on "Homepage" screen
        Then Scroll "Down" into view "Add New Temporary Worker" Section
        Then User clicks "Add Temporary Worker" button on "Temporary Worker" screen
        Then Verify user is on "Add Temporary Worker" screen
        Then User clicks "Add Temporary Worker Form Button" button on "Temporary Worker" screen
        And Verify mandatory fields for "Temporary Worker" screen


    @TemporaryWorkerAdd @Regression @Sanity
    Scenario: Add new temporary worker
        Given Go to the "Base" url
        Then Verify user is on "Login" screen
        When User fills "Valid" form data on "login" screen
        Then Verify user is on "HomePage" screen
        Then User clicks "Temporary Worker" button on "Homepage" screen
        Then Scroll "Down" into view "Add New Temporary Worker" Section
        Then User clicks "Add Temporary Worker" button on "Temporary Worker" screen
        Then User fills "All" form data on "Temporary Worker" screen
        Then User clicks "Temporary Worker Back Button" button on "Temporary Worker" screen
        And Verify record is present on the top of table


    @TemporaryWorkerDeleteLast @Regression @Sanity
    Scenario: Delete Last Temporary worker
        Given Go to the "Base" url
        Then Verify user is on "Login" screen
        When User fills "Valid" form data on "login" screen
        Then Verify user is on "HomePage" screen
        Then User clicks "Temporary Worker" button on "Homepage" screen
        Then Scroll "Down" into view "Add New Temporary Worker" Section
        And User select the Last Item and Tap on Delete Button
        Then User should see a "Temporary Worker Deleted" message

    @TemporaryWorkerDeleteFirst @Regression @Sanity
    Scenario: Delete First Temporary worker
        Given Go to the "Base" url
        Then Verify user is on "Login" screen
        When User fills "Valid" form data on "login" screen
        Then Verify user is on "HomePage" screen
        Then User clicks "Temporary Worker" button on "Homepage" screen
        Then Scroll "Down" into view "Add New Temporary Worker" Section
        And User select the First Item and Tap on Delete Button
        Then User should see a "Temporary Worker Deleted" message

    @TemporaryWorkerCheckButtonsVisible @Regression
    Scenario: Check All Necessary Buttons Visible
        Given Go to the "Base" url
        Then Verify user is on "Login" screen
        When User fills "Valid" form data on "login" screen
        Then Verify user is on "HomePage" screen
        Then User clicks "Temporary Worker" button on "Homepage" screen
        Then Scroll "Down" into view "Add New Temporary Worker" Section
        And Check if All Necessary Buttons are visible