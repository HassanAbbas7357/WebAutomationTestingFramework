TemproryworkersMainLink_xpath = '//a[text()="Temporary Workers"]/parent::li'
AddNewWorker_xpath = '//a[text()="Add New Temporary Worker"]'
AddWorkerHeading_xpath = '//h5[text()="Add new Temporary Worker"]'

# form locators

# personal Details locators
PersonalDetails_xpath = '//h2[text()=" Personal Details "]'
FirstName_xpath = '//input[@placeholder="Enter First Name"]'
LastName_xpath = '//input[@placeholder="Enter Last Name"]'
Select_Nationality_xpath = '//input[@id="register_nationality"]'
CountryName_xpath = lambda x: f'//div[@class="ant-select-item-option-content" and text()="{x}"]'
PhoneNumber_CountryFlagIcon_xpath = '//div[@class="flag nl"]/div[@class="arrow"]'
PhoneNumberCountry_searchInput = '//ul[@class="country-list "]/li//input[@class="search-box"]'  # find Country
PhoneNumberCountryNameClick = lambda \
        x: f'//li[@class="country highlight"]//span[@class="country-name" and text()="{x}"]'
PhoneNumberInput_xpath = '//input[@placeholder="Enter Phone Number"]'
address_xpath = '//textarea[@placeholder="Enter Address"]'
email_xpath = '//input[@placeholder="Enter Email Address"]'

# Employee Status
EmployeeStatusHeading_xpath = '//h2[text()=" Employee Status "]'
EmployeeTypeInput_xpath = '//input[@id="register_employee_type"]'
EmployeeTypeSelect_xpath = lambda x: f'//div[@class="ant-select-item-option-content" and text()="{x}"]'
ContractTypeInleen_xpath = '//span[text()="Inleen/Dorleen"]'
ContractTypeVeritec_xpath = '//span[text()="Veritec"]'
WorkStatus_xpath = '//input[@id="register_worker_status"]'
startDate_xpath = '//input[@id="register_start_date"]'

# Client And Project
ClientAndProjectHeading_xpath = '//h2[text()=" Client & Project "]'
AssignClient_xpath = '//input[@id="register_client_id"]/parent::span/parent::div'
AssignClientsList_xpath = '//label[@title="Assign Client"]/parent::div/parent::div//div[' \
                          '@class="rc-virtual-list-holder-inner"]//div[@class="ant-select-item-option-content"]'
AssignProject_xpath = '//input[@id="register_project_id"]'
AssignProjectsList_xpath = '//label[@title="Assign Project"]/parent::div/parent::div//' \
                           'div[@class="rc-virtual-list-holder-inner"]//div[@class="ant-select-item-option-content"]'

# Residence
ResidenceHeading_xpath = '//h2[text()=" Residence "]'
HouseCheckBox_xpath = lambda \
        x: f'//h2[text()=" Residence "]/parent::div//input[@class="ant-radio-input" and @value="{x}"]'

HouseNameInputSelect_xpath = '//input[@id="register_residence_id"]'
HouseNameList_xpath = '//label[@title="House Name"]/parent::div/parent::div//div[' \
                      '@class="rc-virtual-list-holder-inner"]//div[@class="ant-select-item-option-content"]'
HouseBedInputSelect_xpath = '//input[@id="register_bed_number"]'
HouseBedList_xpath = '//label[@title="House Bed #"]/parent::div/parent::div/parent::div//div[' \
                     '@class="rc-virtual-list-holder-inner"]//div[@class="ant-select-item-option-content"]'
# Transport
TransportHeading_xpath = '//h2[text()=" Transport "]'
TransportYes_xapth = '//label[@title="Transport"]/parent::div/parent::div//input[@class="ant-radio-input" and ' \
                     '@value="true"]'
TransportNO_xapth = '//label[@title="Transport"]/parent::div/parent::div//input[@class="ant-radio-input" and ' \
                    '@value="false"]'
OwnCarYes_xapth = '//label[@title="Own Car"]/parent::div/parent::div//input[@class="ant-radio-input" and ' \
                  '@value="true"]'
OwnCarNO_xapth = '//label[@title="Own Car"]/parent::div/parent::div//input[@class="ant-radio-input" and ' \
                 '@value="false"]'
TypeTransportBike_xpath = '//label[text()="Type of Transport"]/parent::div/following-sibling::div//span[text(' \
                          ')="Bike"]/parent::label//input[@type="radio"]'
TypeTransportCar_xapth = '//label[text()="Type of Transport"]/parent::div/following-sibling::div//span[text(' \
                         ')="Car"]/parent::label//input[@type="radio"]'
NameBikeInput_xpath = '//span[text()="Select Bike"]/parent::div//input[@id="register_transport_id"]'
BikeNameList_xpath = '//label[@title="Name of Bike"]/parent::div/parent::div//div[' \
                     '@class="rc-virtual-list-holder-inner"]//div[@class="ant-select-item-option-content"]'
# Others
OthersHeading_xpath = '//h2[text()=" Others "]'
VCA_YES_xpath = '//div[@id="register_is_vca"]//input[@value="true"]'
VCA_NO_xpath = '//div[@id="register_is_vca"]//input[@value="false"]'
VCAStatusInput = '//label[text()="VCA(status)"]/parent::div/parent::div//input[@id="register_vca_status"]'
VCAStatusList = '//label[@title="VCA(status)"]/parent::div/parent::div//div[' \
                '@class="rc-virtual-list-holder-inner"]//div[@class="ant-select-item-option-content"]'
VCA_ValidUntil = '//input[@id="register_vca_valid_till"]'
VCA_Insurance = '//input[@id="register_has_insurance"]'
VCA_InsuranceList_xpath = '//label[@title="Insurance"]/parent::div/parent::div//div[' \
                          '@class="rc-virtual-list-holder-inner"]//div[@class="ant-select-item-option-content"]'
VCA_DocumentFile_xpath = '//label[@title="VCA Document"]/parent::div/parent::div//input[@type="file"]'

# Add remark Btn
AddRemarkButton_xpath = '//span[contains(text(),"Add remark")]'
RemarkIframe_xpath = '//div[@role="dialog"]'
remarksDate_xpath = '//input[@id="remarksForm_date"]'
statusInput_xpath = '//input[@id="remarksForm_status"]'
status_dropDownList_xpath = '//label[@title="Status"]/parent::div/parent::div//div[' \
                            '@class="rc-virtual-list-holder-inner"]//div[@class="ant-select-item-option-content"]'
remarksTextareaInput_xpath = '//textarea[@id="remarksForm_remark"]'
addRemarksBtn_xpath = '//button[text()=" Add Remark"]'
AddTemporaryButton_xpath = '//button[text()=" Add Temporary Worker"]'
TemporaryDataSave_SuccessMessage_xpath = '//span[text()="Temporary Worker Added Successfully"]'

BACKButton_xpath = '//button[@class="back-button text-"]'
# Table Xpath =

# sort table
TableLoader_xpath = '//span[@class="ant-spin-dot ant-spin-dot-spin"]'
sortTableByID_xpath = '//th//span[@class="ant-table-column-title" and text()="ID"]/parent::div'

TableRow_xpath = lambda title, index=0: f'(//tbody[@class="ant-table-tbody"]//tr[@class="ant-table-row ' \
                                        f'ant-table-row-level-0"])[{index + 1}]//td[@title="{title}"]'
TextRow_xpath = lambda text, index=0: f'(//tbody[@class="ant-table-tbody"]//tr[@class="ant-table-row ' \
                                      f'ant-table-row-level-0"])[{index + 1}]' \
                                      f'//td[text()="{text}"]'

tableRowData_xpath = lambda index=0: f'(//tbody[@class="ant-table-tbody"]//tr[@class="ant-table-row ' \
                                     f'ant-table-row-level-0"])[{index + 1}]//td[not(.//label[' \
                                     f'@class="ant-radio-wrapper"])]'

nextPage = '//li[@title="Next Page"]'
# MainPage Elements
mainTemporaryTable_xpath = '//table'
mainRowRadioButton = '(//tbody[@class="ant-table-tbody"]//tr[@class="ant-table-row ant-table-row-level-0"])[' \
                     '1]//input[@type="radio"]'
mainDeleteButton = '//a[text()="Delete"]'
mainEditButton = '//a[text()="Edit"]'
mainFilterButton = '//a[text()="Filter"]'
mainExportButton = '//a[text()="Export"]'
csvFileEXPORTNAME = '//a[text()="Export"]'
mainShowHideButton = '//a[text()="Show/Hide"]'
mainDeleteYesButton = '//div[@class="ant-modal-content"]//button//span[text()="Yes"]/parent::button'
mainTemporaryDelete_SuccessMessage_xpath = '//span[text()="Temporary Worker Deleted Successfully"]'

# Notifications

AssignProjectBtn_xpath = '//div[text()="Workers without Project"]/parent::div/parent::div//button'
AssignBedBtn_xpath = '//div[text()="Workers without Bed"]/parent::div/parent::div//button'
AssignTransportBtn_xpath = '//div[text()="Workers without Transport"]/parent::div/parent::div//button'
AssignInsuranceBtn_xpath = '//div[text()="Workers without Insurance"]/parent::div/parent::div//button'
