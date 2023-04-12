Feature: Login Feature


  @SignInThroughValidCredentials @Regression @Sanity
  Scenario: Sign in with valid credentials
    Given Go to the "Base" url
    Then Verify user is on "Login" screen
    When User fills "Valid" form data on "login" screen
    Then Verify user is on "HomePage" screen

  @SignInThroughInValidCredentials @Regression @Sanity
  Scenario: Sign in with Invalid credentials
    Given Go to the "Base" url
    When Verify user is on "Login" screen
    And User fills "InValid" form data on "login" screen
    Then User should see an Error "Email Address Or Password Invalid"

  @SignInWithoutCredentials @Regression @Sanity
  Scenario: Sign in without credentials
    Given Go to the "Base" url
    Then Verify user is on "Login" screen
    When User taps on logn button without entering form data
    Then User Should see Erros "Please Enter Your Email!" and "Please Enter Your Password"

  @SignInWithInvalidEmail @Regression @Sanity
  Scenario: Sign in with Invalid email
    Given Go to the "Base" url
    Then Verify user is on "Login" screen
    When User fills "InValid Email" form data on "login" screen
    Then User Should see an error "The input is not valid E-mail!"


  @SignInWithoutPassword @Regression @Sanity
  Scenario: Sign in without Password
    Given Go to the "Base" url
    Then Verify user is on "Login" screen
    When User fills "Empty Password" form data on "login" screen