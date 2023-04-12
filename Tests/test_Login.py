from conftest import *
from base_helpers import *
from Locators.LoginLocators import *


@allure.feature("Login Feature")
@allure.story("Sign in with valid credentials")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
@pytest.mark.sanity
@pytest.mark.smoke
def test_SignInThroughValidCredentials(driver):
    loginUrl = 'http://52.70.226.96:85/login'

    with allure.step('Given Go to the "Base" url'):
        visitUrl(Storage.baseUrl, driver)

    with allure.step('Then Verify user is on Login screen'):
        check_IFRedirectedON_ValidUrl(loginUrl, driver)

    with allure.step('When User fills "Valid" form data on "login" screen'):
        find_byXpath(email_xpath, driver).send_keys(Storage.userData1['Email'])
        find_byXpath(password_xpath, driver).send_keys(
            Storage.userData1['Password'])
        find_byXpath(LoginBtn_xpath, driver).click()

    with allure.step('Then Verify user is on "HomePage" screen'):
        verify_element_is_present(Dashboard_Xpath, driver)


@allure.feature("Login Feature")
@allure.story("Sign in with Invalid credentials")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
@pytest.mark.sanity
def test_SignInThroughInValidCredentials(driver):
    loginUrl = 'http://52.70.226.96:85/login'

    with allure.step('Given Go to the "Base" url'):
        visitUrl(Storage.baseUrl, driver)

    with allure.step('Then Verify user is on Login screen'):
        check_IFRedirectedON_ValidUrl(loginUrl, driver)

    with allure.step('When User fills "InValid" form data on "login" screen'):
        find_byXpath(email_xpath, driver).send_keys(Storage.userData2['Email'])
        find_byXpath(password_xpath, driver).send_keys(
            Storage.userData1['Password'])
        find_byXpath(LoginBtn_xpath, driver).click()

    with allure.step('Then User should see an Error "Email Address Or Password Invalid"'):
        verify_element_is_present(loginErrorMessage_xpath, driver)


@allure.feature("Login Feature")
@allure.story("Sign in without credentials")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
@pytest.mark.sanity
def test_SignInWithoutCredentials(driver):
    loginUrl = 'http://52.70.226.96:85/login'

    with allure.step('Given Go to the "Base" url'):
        visitUrl(Storage.baseUrl, driver)

    with allure.step('Then Verify user is on Login screen'):
        check_IFRedirectedON_ValidUrl(loginUrl, driver)

    with allure.step('When User taps on logn button without entering form data'):
        find_byXpath(LoginBtn_xpath, driver).click()

    with allure.step('Then User Should see Erros "Please Enter Your Email!" and "Please Enter Your Password"'):
        verify_element_is_present(EmptyEmailCredentialError_xpath, driver)
        verify_element_is_present(EmptyPasswordCredentialError_xpath, driver)


@allure.feature("Login Feature")
@allure.story("Sign in With Invalid Email")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
@pytest.mark.sanity
def test_SignInWithInvalidEmail(driver):
    loginUrl = 'http://52.70.226.96:85/login'

    with allure.step('Given Go to the "Base" url'):
        visitUrl(Storage.baseUrl, driver)

    with allure.step('Then Verify user is on Login screen'):
        check_IFRedirectedON_ValidUrl(loginUrl, driver)

    with allure.step('When User fills "InValid Email" form data on "login" screen'):
        find_byXpath(email_xpath, driver).send_keys("123ja")

    with allure.step('Then User Should see an error "The input is not valid E-mail!"'):
        verify_element_is_present(InvalidEmailMessage_xpath, driver)


@allure.feature("Login Feature")
@allure.story("Sign in With Invalid Password")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
@pytest.mark.sanity
def test_SignInWithoutPassword(driver):
    loginUrl = 'http://52.70.226.96:85/login'

    with allure.step('Given Go to the "Base" url'):
        visitUrl(Storage.baseUrl, driver)

    with allure.step('Then Verify user is on Login screen'):
        check_IFRedirectedON_ValidUrl(loginUrl, driver)

    with allure.step('When User fills "InValid Password" in form data on "login" screen'):
        find_byXpath(email_xpath, driver).send_keys(Storage.userData1['Email'])
        find_byXpath(password_xpath, driver).send_keys("123ja")
        find_byXpath(LoginBtn_xpath, driver).click()

    with allure.step('Then User Should see an error "Email Address Or Password Invalid"'):
        verify_element_is_present(loginErrorMessage_xpath, driver)


def loginwithSteps(driver):
    test_SignInThroughValidCredentials(driver)
