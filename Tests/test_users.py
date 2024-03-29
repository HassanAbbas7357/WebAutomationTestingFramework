from Locators.TempWorkersLocators import csvFileEXPORTNAME, nextPage, mainShowHideButton, mainExportButton, \
    mainFilterButton, mainRowRadioButton, mainDeleteButton, mainDeleteYesButton, \
    mainTemporaryDelete_SuccessMessage_xpath, TableLoader_xpath
from Tests.test_temprory_worker import downloadAndVerifyCSVExportedFile, sortTableByIdDescendingOrder
from conftest import *
from base_helpers import *
from Locators.UsersLocators import *
from test_Login import loginwithSteps


@allure.feature("Users Feature")
@allure.story("Verify Users Screen Navigation")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@pytest.mark.sanity
def test_UsersScreenNavigation(driver):
    loginwithSteps(driver)
    UsersUrl = 'active-user'
    with allure.step('Then User clicks "Users" button on "Homepage" screen'):
        scroll_into_element(UsersMainLink_xpath, driver)
        find_byXpath(UsersMainLink_xpath, driver).click()
    with allure.step('And User Should see "active-user" in the url'):
        assert UsersUrl in driver.current_url


def VisitUsersPageWithLogin(driver):
    test_UsersScreenNavigation(driver)


@allure.feature("Users Feature")
@allure.story("Check If Export Button actually downloads the file and its in csv format")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@pytest.mark.sanity
@pytest.mark.smoke
@pytest.mark.order(3)
def test_UsersCheckExportButtonDownloadsCSVFile(driver):
    VisitUsersPageWithLogin(driver)
    fileName = downloadAndVerifyCSVExportedFile(driver)
    os.remove(fileName)


@allure.feature("Users Feature")
@allure.story("Verify If Exported CSV Users file has the exact data matches with table")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@pytest.mark.sanity
def test_UsersVerifyIfExportedCSVFileDataMatchesWithWebTableData(driver):
    VisitUsersPageWithLogin(driver)
    with allure.step('And Check if CSV file downloaded correctly'):
        fileName = Storage.downloadsPath + \
            find_byXpath(csvFileEXPORTNAME, driver).get_attribute(
                "download") + '.csv'
        downloadAndVerifyCSVExportedFile(driver)

    with allure.step("Verify If Exported CSV file has the exact data matches with table"):
        scroll_to_bottom_of_page(driver)
        sleep(4)
        df = pd.read_csv(fileName)
        df = df.fillna('')

        counter = 0
        page = 1

        for i, row in df.iterrows():
            if counter == 10:
                print(f'Page : {page + 1}')
                page += 1
                counter = 0
                find_byXpath(nextPage, driver).click()

            csv_list = row.tolist()
            ID = csv_list[0]
            first_name = csv_list[1]
            last_name = csv_list[2]
            email = csv_list[3]
            role = csv_list[4]
            phone_number = csv_list[5]
            created_by = csv_list[6]
            approve_by = csv_list[7]
            status = csv_list[8]

            listOfData = [ID, first_name, last_name, email, role,
                          phone_number, created_by, approve_by, status]

            # noinspection PyTypeChecker
            verifyDatainTableByRow(
                driver, rowData=listOfData, rowIndex=counter)
            counter += 1


@allure.feature("Users Feature")
@allure.story("Navigate to check if Users for approval page is present")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@pytest.mark.sanity
def test_UsersNavigateToUsersForApprovalPage(driver):
    VisitUsersPageWithLogin(driver)
    UsersForApprovalTabUrl = 'approve-user'
    with allure.step('Then User clicks "Users for Approval" button on screen'):
        find_byXpath(UsersForApprovalTab_xpath, driver).click()

    with allure.step('And User Should see "approve-user" in the url'):
        assert UsersForApprovalTabUrl in driver.current_url


@allure.feature("Users Feature")
@allure.story("Check All Necessary Buttons Clickable")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.regression
@pytest.mark.sanity
@pytest.mark.order(4)
def test_UserCheckNecessaryButtonsClickAble(driver):
    VisitUsersPageWithLogin(driver)
    with allure.step('And Check if All Necessary Buttons are Clickable'):
        verify_elementIsClickAble(mainShowHideButton, driver)
        verify_elementIsClickAble(mainExportButton, driver)
        verify_elementIsClickAble(mainFilterButton, driver)


@allure.feature("Users Feature")
@allure.story("Check All Necessary Buttons are Visible")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.regression
@pytest.mark.sanity
@pytest.mark.order(4)
def test_UserCheckNecessaryButtonsVisible(driver):
    VisitUsersPageWithLogin(driver)
    with allure.step('And Check if All Necessary Buttons are Clickable'):
        verify_visibility_of_element_located(mainShowHideButton, driver)
        verify_visibility_of_element_located(mainExportButton, driver)
        verify_visibility_of_element_located(mainFilterButton, driver)


@allure.feature("Users Feature")
@allure.story("Delete Last User And Verify Message")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.regression
@pytest.mark.sanity
def test_UserDeleteLastAndVerify(driver):
    VisitUsersPageWithLogin(driver)
    with allure.step('When User Tap on ID on table to sort it by descending order'):
        verify_loaderAndWait(TableLoader_xpath, driver)
        sortTableByIdDescendingOrder(driver)
    with allure.step('And User select the last Item and Tap on Delete Button'):
        find_byXpath(deleteUser_xpath, driver).click()
        # find_byXpathAndWait(mainDeleteButton, driver).click()
        find_byXpathAndWait(mainDeleteYesButton, driver).click()
    with allure.step('Then User should see a "User Deleted Successfully" message'):
        verify_visibility_of_element_located(userDeletedMessage, driver)


@allure.feature("Users Feature")
@allure.story("Delete First User And Verify Message")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.regression
@pytest.mark.sanity
def test_UserDeleteFirstAndVerify(driver):
    VisitUsersPageWithLogin(driver)
    with allure.step('And User select the last Item and Tap on Delete Button'):
        verify_loaderAndWait(TableLoader_xpath, driver)
        find_byXpathAndWait(deleteUser_xpath, driver).click()
        find_byXpathAndWait(mainDeleteYesButton, driver).click()
    with allure.step('Then User should see a "User Deleted Successfully" message'):
        verify_visibility_of_element_located(userDeletedMessage, driver)


@allure.feature("Users Feature")
@allure.story("Click on Edit User Button And Verify Mandatory FormFields are present")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.regression
@pytest.mark.sanity
def test_verifyEditFormFieldsArePresent(driver):
    VisitUsersPageWithLogin(driver)
    with allure.step('And User Click on Edit Button'):
        find_byXpathAndWait(userEditBtn_xpath, driver).click()
    with allure.step('Then User should see a Form containing mandatory fields'):
        verify_visibility_of_element_located(firstNameInput, driver)
        verify_visibility_of_element_located(lastNameInput, driver)
        verify_visibility_of_element_located(phoneNumberInput, driver)
        verify_visibility_of_element_located(saveChangesButton, driver)


@allure.feature("Users Feature")
@allure.story("Click on Edit User Button And Click On Save Changes button without even changing anything")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.regression
@pytest.mark.sanity
def test_verifyEditFormShowingChangesSavedSuccessWhenSubmittingFormWithoutChanges(driver):
    VisitUsersPageWithLogin(driver)
    with allure.step('And User Click on Edit Button'):
        verify_loaderAndWait(TableLoader_xpath, driver)
        find_byXpathAndWait(userEditBtn_xpath, driver).click()
    with allure.step('Then Click On Save Changes button without even changing anything"'):
        find_byXpathAndWait(saveChangesButton, driver).click()
    with allure.step('And User Should see Success Message "User Updated Successfully"'):
        verify_visibility_of_element_located(invalidUserMessage, driver)


@allure.feature("Users Feature")
@allure.story("Edit the FirstName and Verify in Table")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.regression
@pytest.mark.sanity
def test_EditFirstNameAndVerifyInTable(driver):
    VisitUsersPageWithLogin(driver)
    FirstName = get_randomEmail().replace('@gmail.com', '')
    with allure.step('And User Click on Edit Button'):
        verify_loaderAndWait(TableLoader_xpath, driver)
        find_byXpathAndWait(userEditBtn_xpath, driver).click()
    with allure.step('Then Click On Save Changes button after changing FirstName"'):
        driver.execute_script(
            "arguments[0].value='';", find_byXpath(firstNameInput, driver))
        find_byXpath(firstNameInput, driver).send_keys(FirstName)
        print(FirstName)
        find_byXpathAndWait(saveChangesButton, driver).click()
    with allure.step('And User Should see Success Message "User Updated SuccessFully"'):
        verify_visibility_of_element_located(invalidUserMessage, driver)
        sleep(3)
    with allure.step('Then Verify FirstName Updated in the Table'):
        Name = find_Elements_byXpathAndWait_getText(firstRow, driver)
        print(Name)
        assert FirstName == Name[1]


@allure.feature("Users Feature")
@allure.story("Edit the LastName and Verify in Table")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.regression
@pytest.mark.sanity
def test_EditLastNameAndVerifyInTable(driver):
    VisitUsersPageWithLogin(driver)
    FirstName = get_randomEmail().replace('@gmail.com', '')
    with allure.step('And User Click on Edit Button'):
        verify_loaderAndWait(TableLoader_xpath, driver)
        find_byXpathAndWait(userEditBtn_xpath, driver).click()
    with allure.step('Then Click On Save Changes button after changing LastName"'):
        driver.execute_script(
            "arguments[0].value='';", find_byXpath(lastNameInput, driver))
        find_byXpath(lastNameInput, driver).send_keys(FirstName)
        print(FirstName)
        find_byXpathAndWait(saveChangesButton, driver).click()
    with allure.step('And User Should see Success Message "User Updated SuccessFully"'):
        verify_visibility_of_element_located(invalidUserMessage, driver)
        sleep(3)
    with allure.step('Then Verify LastName Updated in the Table'):
        Name = find_Elements_byXpathAndWait_getText(firstRow, driver)
        print(Name)
        assert FirstName == Name[2]


def visitAddUserScreenWithLoginSteps(driver):
    VisitUsersPageWithLogin(driver)
    AddUserUrl = '/user/add'
    with allure.step('And User Click on Add User Button'):
        # verify_loaderAndWait(TableLoader_xpath, driver)
        scroll_to_bottom_of_page(driver)
        find_byXpath(addNewUserMain_xpath, driver).click()
    with allure.step('And Verify User is on UserAdd Screen'):
        assert AddUserUrl in driver.current_url


@allure.feature("Users Feature")
@allure.story("Add New User Screen Click Submit Button And Verify Errors")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.regression
@pytest.mark.sanity
def test_AddAndVerifyErrors(driver):
    visitAddUserScreenWithLoginSteps(driver)

    with allure.step('When User Clicks on AddUser Button'):
        find_byXpath(AddUserButton, driver).click()
    with allure.step('Then User Should See Please Input message for all the required fields'):
        verify_visibility_of_element_located("//div[@class='ant-form-item-explain-error' and text()='Please input "
                                             "your first name!']", driver)
        verify_visibility_of_element_located("//div[@class='ant-form-item-explain-error' and text()='Please input "
                                             "your last name']", driver)
        verify_visibility_of_element_located("//div[@class='ant-form-item-explain-error' and text()='Please input "
                                             "your phone number!']", driver)
        verify_visibility_of_element_located("//div[@class='ant-form-item-explain-error' and text()='Please Enter "
                                             "Your Email!']", driver)
        verify_visibility_of_element_located("//div[@class='ant-form-item-explain-error' and text()='Please Select "
                                             "user role!']", driver)


@allure.feature("Users Feature")
@allure.story("Add New User And Verify In Table")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.regression
@pytest.mark.sanity
def test_AddNewUserAndVerify(driver):
    visitAddUserScreenWithLoginSteps(driver)

    with allure.step('When User Inputs Fills Form with Valid Data'):
        find_byXpath(firstNameInput, driver).send_keys("Bot")
        find_byXpath(lastNameInput, driver).send_keys("Hassan")
        find_byXpath(Email_xpath, driver).send_keys(get_randomEmail())
        find_byXpath(phoneInput, driver).send_keys("+923163466125")
        find_byXpath(roleClickField, driver).click()
        find_byXpathAndWait(selectAdmin, driver).click()
        find_byXpath(inActiveRadioBtn, driver).click()

    with allure.step('When User Clicks on AddUser Button'):
        find_byXpath(AddUserButton, driver).click()

    with allure.step('Then User Should see "User Added Successfully" message'):
        verify_visibility_of_element_located(userAddedMessage, driver)
