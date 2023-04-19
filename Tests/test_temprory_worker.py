from flaky import flaky
from conftest import *
from base_helpers import *
from Locators.TempWorkersLocators import *
from test_Login import loginwithSteps
from API_Helpers import populate_Bike, populate_Car

TW = Storage.temporaryWorkerData
Email = TW.Email


@allure.feature("Temporary Worker Feature")
@allure.story("Add new temporary worker Screen")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@pytest.mark.sanity
def test_TemporaryWorkerScreen(driver):
    loginwithSteps(driver)
    with allure.step('Then User clicks "Temporary Worker" button on "Homepage" screen'):
        find_byXpath(TemproryworkersMainLink_xpath, driver).click()

    with allure.step('Then Scroll "Down" into view "Add New Temporary Worker" Section'):
        scroll_into_element(AddNewWorker_xpath, driver)

    with allure.step('Then User clicks "Add Temporary Worker" button on "Temporary Worker" screen'):
        find_byXpath(AddNewWorker_xpath, driver).click()

    with allure.step('Then Verify user is on "Add Temporary Worker" screen'):
        check_IFRedirectedON_ValidUrl(Storage.temporaryWorkerUrlAdd, driver)


def VisitTemporary_WorkerPageWithSteps(driver):
    test_TemporaryWorkerScreen(driver)


def VisitTemporaryWorkerPageWithLogin(driver):
    loginwithSteps(driver)
    visitUrl(Storage.temporaryWorkerUrl, driver)

    with allure.step('Then User clicks "Temporary Worker" button on "Homepage" screen'):
        find_byXpath(TemproryworkersMainLink_xpath, driver).click()


def downloadAndVerifyCSVExportedFile(driver):
    with allure.step('And Check if CSV file downloaded correctly'):
        verify_loaderAndWait(TableLoader_xpath, driver)
        sleep(2)
        verify_elementIsClickAble(mainExportButton, driver)
        find_byXpath(mainExportButton, driver).click()
        print('Downloading the file now')
        sleep(4)
        fileName = Storage.downloadsPath + find_byXpath(csvFileEXPORTNAME, driver).get_attribute("download") + '.csv'
        verifyFileDownloadedCorrectly(FilePath=fileName)
        return fileName


@allure.feature("Temporary Worker Feature")
@allure.story("Verify All mandatory fields for Temporary Worker Screen")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@pytest.mark.sanity
def test_TemporaryWorkerMandatoryFields(driver):
    VisitTemporary_WorkerPageWithSteps(driver)
    with allure.step('And Verify All mandatory fields for "Temporary Worker" screen'):
        # Personal Details
        verify_element_is_present(PersonalDetails_xpath, driver)
        verify_element_is_present(AddWorkerHeading_xpath, driver)
        verify_element_is_present(FirstName_xpath, driver)
        verify_element_is_present(LastName_xpath, driver)
        verify_element_is_present(Select_Nationality_xpath, driver)
        verify_element_is_present(PhoneNumberInput_xpath, driver)
        verify_element_is_present(PhoneNumber_CountryFlagIcon_xpath, driver)
        # verify_element_is_present(address_xpath, driver)
        verify_element_is_present(email_xpath, driver)
        # Employee Status
        verify_element_is_present(EmployeeStatusHeading_xpath, driver)
        verify_element_is_present(EmployeeTypeInput_xpath, driver)
        verify_element_is_present(ContractTypeInleen_xpath, driver)
        verify_element_is_present(ContractTypeVeritec_xpath, driver)
        verify_element_is_present(WorkStatus_xpath, driver)
        verify_element_is_present(startDate_xpath, driver)
        # Client And Project
        verify_element_is_present(ClientAndProjectHeading_xpath, driver)
        verify_element_is_present(AssignClient_xpath, driver)
        verify_element_is_present(AssignProject_xpath, driver)
        # Residence
        verify_element_is_present(ResidenceHeading_xpath, driver)
        verify_element_is_present(HouseCheckBox_xpath(TW.HouseCheckBOX), driver)
        verify_element_is_present(HouseNameInputSelect_xpath, driver)
        verify_element_is_present(HouseBedInputSelect_xpath, driver)
        # Transport
        verify_element_is_present(TransportHeading_xpath, driver)
        verify_element_is_present(TransportYes_xapth, driver)
        verify_element_is_present(TransportNO_xapth, driver)
        verify_element_is_present(OwnCarYes_xapth, driver)
        verify_element_is_present(OwnCarNO_xapth, driver)
        verify_element_is_present(TypeTransportBike_xpath, driver)
        verify_element_is_present(TypeTransportCar_xapth, driver)
        # Others
        verify_element_is_present(OthersHeading_xpath, driver)
        verify_element_is_present(VCA_YES_xpath, driver)
        verify_element_is_present(VCA_NO_xpath, driver)
        verify_element_is_present(VCA_DocumentFile_xpath, driver)
        verify_element_is_present(AddRemarkButton_xpath, driver)


def fillUserPersonalData(driver):
    with allure.step('Enter Personal Data'):
        find_byXpath(FirstName_xpath, driver).send_keys(TW.FirstName)
        find_byXpath(LastName_xpath, driver).send_keys(TW.LastName)
        find_byXpath(Select_Nationality_xpath, driver).click()
        sleep(1)
        find_byXpath(Select_Nationality_xpath, driver).send_keys(TW.Nationality)
        find_byXpathAndWait(CountryName_xpath(TW.Nationality), driver).click()
        find_byXpath(PhoneNumber_CountryFlagIcon_xpath, driver).click()
        find_byXpath(PhoneNumberCountry_searchInput, driver).send_keys(TW.PhoneCountry)
        find_byXpath(PhoneNumberCountryNameClick(TW.PhoneCountry), driver).click()
        find_byXpath(PhoneNumberInput_xpath, driver).click()
        find_byXpath(PhoneNumberInput_xpath, driver).send_keys(TW.PhoneNumber)
        # find_byXpath(address_xpath, driver).send_keys(TW.Address)

        find_byXpath(email_xpath, driver).send_keys(Email)
        scroll_into_element(email_xpath, driver)


def fillEmployeeStatus(driver):
    with allure.step('Enter Employee Status'):
        find_byXpath(EmployeeTypeInput_xpath, driver).click()
        find_byXpathAndWait(EmployeeTypeInput_xpath, driver).send_keys(TW.EmployeeType)
        find_byXpath(EmployeeTypeSelect_xpath(TW.EmployeeType), driver).click()
        if find_byXpath(ContractTypeInleen_xpath, driver).is_selected():
            pass
        else:
            find_byXpath(ContractTypeInleen_xpath, driver).click()
        scroll_into_element(EmployeeStatusHeading_xpath, driver)
        find_byXpath(startDate_xpath, driver).click()
        find_byXpath(startDate_xpath, driver).send_keys(TW.StartDate)
        press_Enter(driver)


def fillClientAndProjectInfo(driver):
    with allure.step('Enter Client & Project Information'):
        scroll_into_element(ClientAndProjectHeading_xpath, driver)
        click_on_element_js(AssignClient_xpath, driver)
        sleep(3)
        TW.Client = find_Elements_byXpathAndWait_getText(AssignClientsList_xpath, driver)[1]
        find_Elements_byXpathAndWait(AssignClientsList_xpath, driver)[1].click()
        find_byXpath(AssignProject_xpath, driver).click()
        TW.Project = find_Elements_byXpathAndWait_getText(AssignProjectsList_xpath, driver)[1]
        find_Elements_byXpathAndWait(AssignProjectsList_xpath, driver)[1].click()


def fillResidenceInfo(driver):
    with allure.step('Enter Residence Information'):
        scroll_into_element(ResidenceHeading_xpath, driver)
        click_on_element_js(HouseCheckBox_xpath(TW.HouseCheckBOX), driver)
        click_on_element_js(HouseNameInputSelect_xpath, driver)
        TW.HouseName = find_Elements_byXpathAndWait_getText(HouseNameList_xpath, driver)[0]
        find_Elements_byXpathAndWait(HouseNameList_xpath, driver)[0].click()
        find_byXpathAndWait(HouseBedInputSelect_xpath, driver).click()
        TW.BedNumber = find_Elements_byXpathAndWait_getText(HouseBedList_xpath, driver)[0]
        find_Elements_byXpathAndWait(HouseBedList_xpath, driver)[0].click()


def fillTransportInfo(driver):
    with allure.step('Enter Transport Information'):
        scroll_into_element(TransportHeading_xpath, driver)
        click_on_element_js(TransportYes_xapth, driver)
        click_on_element_js(TypeTransportBike_xpath, driver)
        find_byXpath(NameBikeInput_xpath, driver).click()
        sleep(1)
        TW.BikeNameOrLicencePlate = find_Elements_byXpathAndWait_getText(BikeNameList_xpath, driver)[0]
        find_Elements_byXpathAndWait(BikeNameList_xpath, driver)[0].click()


def fillOthersInfo(driver, file=False):
    with allure.step('Enter Other Information and Upload File'):
        find_byXpath(VCA_YES_xpath, driver).click()
        find_byXpath(VCAStatusInput, driver).click()
        TW.VCA_Status = find_Elements_byXpathAndWait_getText(VCAStatusList, driver)[0]
        find_Elements_byXpath(VCAStatusList, driver)[0].click()
        find_byXpath(VCA_ValidUntil, driver).click()
        find_byXpath(VCA_ValidUntil, driver).send_keys(TW.StartDate)
        press_Enter(driver)
        find_byXpath(VCA_Insurance, driver).click()
        TW.VCA_Insurance = find_Elements_byXpathAndWait_getText(VCA_InsuranceList_xpath, driver)[1]
        find_Elements_byXpath(VCA_InsuranceList_xpath, driver)[1].click()
        print(TW.filepath)
        if file:
            find_byXpath(VCA_DocumentFile_xpath, driver).send_keys(TW.filepath)


def fillAndHandleRemarksInfo(driver):
    with allure.step('Handle Remarks Popup and Add Remarks'):
        TW.Email = get_randomEmail()
        find_byXpath(AddRemarkButton_xpath, driver).click()
        verify_element_is_present(RemarkIframe_xpath, driver)
        sleep(1)
        find_byXpathAndWait(remarksDate_xpath, driver).click()
        find_byXpathAndWait(remarksDate_xpath, driver).send_keys(TW.StartDate)
        press_Enter(driver)
        sleep(1)
        find_byXpathAndWait(statusInput_xpath, driver).click()
        find_Elements_byXpath(status_dropDownList_xpath, driver)[0].click()
        find_byXpath(remarksTextareaInput_xpath, driver).send_keys(TW.remarks)
        find_byXpath(addRemarksBtn_xpath, driver).click()


def saveAndVerifyIfInfoSaved(driver):
    with allure.step('Click Add Temporary Button to save information'):
        click_on_element_js(AddTemporaryButton_xpath, driver)
    with allure.step('Verify from Success popup-message'):
        verify_visibility_of_element_located(TemporaryDataSave_SuccessMessage_xpath, driver)


def sortTableByIdDescendingOrder(driver):
    scroll_into_element(mainTemporaryTable_xpath, driver)
    verify_loaderAndWait(TableLoader_xpath, driver)
    find_byXpathAndWait(sortTableByID_xpath, driver).click()
    sleep(1)
    find_byXpathAndWait(sortTableByID_xpath, driver).click()


def verifyDataInTable(driver, textPathList, tableDataList, tableIndex=0):
    with allure.step(f'Verify Data in Table: {textPathList} {tableDataList}'):
        # scroll_into_element(BACKButton_xpath, driver)
        # click_on_element_js(BACKButton_xpath, driver)
        # sleep(2)
        # sortTableByIdDescendingOrder(driver)
        # assert find_byXpathAndGet_text(TextRow_xpath(Email), driver) == Email
        verify_Data_TableCell_ByTextXpath(driver,
                                          textPathList, tableIndex)
        verify_Data_TableCell(driver,
                              tableDataList, tableIndex)


@allure.feature("Temporary Worker Feature")
@allure.story("Add new temporary worker")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@pytest.mark.sanity
@flaky
def test_TemporaryWorkerAdd(driver):
    global Email
    VisitTemporary_WorkerPageWithSteps(driver)
    populate_Bike()
    populate_Car()
    with allure.step('Then User fills "All" form data on "Temporary Worker" screen'):
        fillUserPersonalData(driver)
        fillEmployeeStatus(driver)
        fillClientAndProjectInfo(driver)
        fillResidenceInfo(driver)
        fillTransportInfo(driver)
        fillOthersInfo(driver, file=True)
        fillAndHandleRemarksInfo(driver)
        saveAndVerifyIfInfoSaved(driver)
        click_on_element_js(BACKButton_xpath, driver)
        sleep(2)
        sortTableByIdDescendingOrder(driver)
        verifyDataInTable(driver,
                          textPathList=[Email, TW.BedNumber, TW.TransportType, TW.VCA_Status],
                          tableDataList=[
                              TW.FirstName, TW.LastName, f'92{TW.PhoneNumber}', TW.Nationality, TW.Address,
                              TW.EmployeeType, TW.Client, TW.Project, replace_string(TW.House),
                              TW.BikeNameOrLicencePlate, TW.VCA_Insurance
                          ])


@allure.feature("Temporary Worker Feature")
@allure.story("Delete Last Temporary worker")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@pytest.mark.sanity
def test_TemporaryWorkerDeleteLast(driver):
    VisitTemporaryWorkerPageWithLogin(driver)
    with allure.step('When User Tap on ID on table to sort it by descending order'):
        sortTableByIdDescendingOrder(driver)
    with allure.step('And User select the last Item and Tap on Delete Button'):
        find_byXpath(mainRowRadioButton, driver).click()
        find_byXpath(mainDeleteButton, driver).click()
        find_byXpathAndWait(mainDeleteYesButton, driver).click()
    with allure.step('Then User should see a "Temporary Worker Deleted" message'):
        verify_visibility_of_element_located(mainTemporaryDelete_SuccessMessage_xpath, driver)


@allure.feature("Temporary Worker Feature")
@allure.story("Delete First Temporary worker")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@pytest.mark.sanity
@pytest.mark.order(1)
def test_TemporaryWorkerDeleteLast(driver):
    VisitTemporaryWorkerPageWithLogin(driver)
    sortTableByIdDescendingOrder(driver)
    with allure.step('And User select the last Item and Tap on Delete Button'):
        find_byXpath(mainRowRadioButton, driver).click()
        find_byXpath(mainDeleteButton, driver).click()
        find_byXpathAndWait(mainDeleteYesButton, driver).click()
    with allure.step('Then User should see a "Temporary Worker Deleted" message'):
        verify_visibility_of_element_located(mainTemporaryDelete_SuccessMessage_xpath, driver)


@allure.feature("Temporary Worker Feature")
@allure.story("Delete Last Temporary worker")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@pytest.mark.sanity
@pytest.mark.order(2)
def test_TemporaryWorkerDeleteFirst(driver):
    VisitTemporaryWorkerPageWithLogin(driver)
    scroll_into_element(mainTemporaryTable_xpath, driver)
    verify_loaderAndWait(TableLoader_xpath, driver)
    with allure.step('And User select the First Item and Tap on Delete Button'):
        find_byXpath(mainRowRadioButton, driver).click()
        find_byXpath(mainDeleteButton, driver).click()
        find_byXpathAndWait(mainDeleteYesButton, driver).click()
    with allure.step('Then User should see a "Temporary Worker Deleted" message'):
        verify_visibility_of_element_located(mainTemporaryDelete_SuccessMessage_xpath, driver)


@allure.feature("Temporary Worker Feature")
@allure.story("Check All Necessary Buttons Visible")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.regression
@pytest.mark.sanity
def test_TemporaryWorkerCheckNecessaryButtonsVisible(driver):
    VisitTemporaryWorkerPageWithLogin(driver)
    with allure.step('And Check if All Necessary Buttons are visible'):
        verify_visibility_of_element_located(mainDeleteButton, driver)
        verify_visibility_of_element_located(mainEditButton, driver)
        verify_visibility_of_element_located(mainShowHideButton, driver)
        verify_visibility_of_element_located(mainExportButton, driver)
        verify_visibility_of_element_located(mainFilterButton, driver)


@allure.feature("Temporary Worker Feature")
@allure.story("Check All Necessary Buttons Clickable")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.regression
@pytest.mark.sanity
@pytest.mark.order(4)
def test_TemporaryWorkerCheckNecessaryButtonsClickAble(driver):
    VisitTemporaryWorkerPageWithLogin(driver)
    with allure.step('And Check if All Necessary Buttons are Clickable'):
        verify_elementIsClickAble(mainDeleteButton, driver)
        verify_elementIsClickAble(mainEditButton, driver)
        verify_elementIsClickAble(mainShowHideButton, driver)
        verify_elementIsClickAble(mainExportButton, driver)
        verify_elementIsClickAble(mainFilterButton, driver)


@allure.feature("Temporary Worker Feature")
@allure.story("Check If Export Button actually downloads the file and its in csv format")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@pytest.mark.sanity
# @pytest.mark.smoke
@pytest.mark.order(3)
def test_TemporaryWorkerCheckExportButtonDownloadsCSVFile(driver):
    VisitTemporaryWorkerPageWithLogin(driver)
    fileName = downloadAndVerifyCSVExportedFile(driver)
    os.remove(fileName)


@allure.feature("Temporary Worker Feature")
@allure.story("Verify If Exported CSV file has the exact data matches with table")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@pytest.mark.sanity
@pytest.mark.order(5)
def test_TemporaryWorkerVerifyIfExportedCSVFileDataMatchesWithWebTableData(driver):
    VisitTemporaryWorkerPageWithLogin(driver)

    fileName = Storage.downloadsPath + find_byXpath(csvFileEXPORTNAME, driver).get_attribute("download") + '.csv'
    downloadAndVerifyCSVExportedFile(driver)

    with allure.step("Verify If Exported CSV file has the exact data matches with table"):
        scroll_to_bottom_of_page(driver)
        sleep(4)
        df = pd.read_csv(fileName)
        df = df.fillna('')
        df = df.replace(True, "Yes")
        df = df.replace(False, "No")
        df["VCA Valid Until"] = pd.to_datetime(df["VCA Valid Until"])
        df["VCA Valid Until"] = df["VCA Valid Until"].dt.strftime("%d-%b-%Y")

        counter = 0
        page = 1

        for i, row in df.iterrows():
            if counter == 10:
                print(f'Page : {page + 1}')
                page += 1
                counter = 0
                find_byXpath(nextPage, driver).click()

            csv_list = row.tolist()
            ID = str(csv_list[0])
            firstName = csv_list[1]
            lastName = csv_list[2]
            email = csv_list[3]
            status = csv_list[4]
            phoneNumber = csv_list[5]
            nationality = csv_list[6]
            #address = csv_list[7]
            employeeType = csv_list[7]
            contractType = csv_list[8]
            client = csv_list[9]
            project = csv_list[10]
            house = csv_list[11]
            houseName = csv_list[12]
            houseBed = csv_list[13]
            transport = csv_list[14]
            transportType = csv_list[15]
            licensePlateNumber = csv_list[16]
            seatNumber = csv_list[17]
            ddriver = csv_list[18]
            licenseEndDate = csv_list[19]
            vca = csv_list[20]
            vcaStatus = csv_list[21]
            vcaValidUntil = csv_list[22]
            insurance = csv_list[23]
            statusReason = csv_list[24]

            listOfData = [ID, firstName, lastName, email, status, phoneNumber, nationality, employeeType,
                          contractType, client, project, house, houseName, houseBed, transport, transportType,
                          licensePlateNumber, seatNumber, ddriver, licenseEndDate, vca, vcaStatus, vcaValidUntil,
                          insurance, statusReason]
            # noinspection PyTypeChecker
            verifyDatainTableByRow(driver, rowData=listOfData, rowIndex=counter)
            counter += 1


