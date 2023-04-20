# import pytest
# from pytest import fixture
# from conftest import *
from base_helpers import *
import os
from base_helpers import get_randomEmail


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "regression: mark test as a regression test")
    config.addinivalue_line("markers", "smoke: mark test as a smoke test")
    config.addinivalue_line("markers", "sanity: mark test as a sanity test")


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="CHROME"
    )
    parser.addoption(
        "--headless", action="store"
    )


class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


class TemoraryWorkerDataClass:
    FirstName = 'Terminator'
    LastName = 'Genesis'
    Nationality = 'Pakistani'
    PhoneCountry = 'Pakistan'
    PhoneNumber = '3058440922'
    Address = 'Chandigarh road mia wali AirPush karachi Sindhi'
    Email = get_randomEmail()
    EmployeeType = 'Temporary Worker'
    Client = None
    Project = None
    Contract_Type = 'Inleen Dorleen'
    House = 'Yes'
    HouseCheckBOX = "true"
    HouseName = None
    TransportType = 'Bike'
    BedNumber = None
    BikeNameOrLicencePlate = None
    VCA_Status = None
    VCA_Insurance = None
    StartDate = '30-APR-2023'
    filepath = os.getcwd() + '/TestData/terminator.jpeg'
    remarks = 'Quality Assurance, is a critical process in software development that ensures the final product'


class Storage:
    baseUrl = 'http://52.70.226.96:85'
    downloadsPath = os.getcwd() + '/Downloads/'
    temporaryWorkerData = TemoraryWorkerDataClass()
    temporaryWorkerUrlAdd = 'http://52.70.226.96:85/temporary-worker/add'
    temporaryWorkerUrl = 'http://52.70.226.96:85/temporary-worker'
    userData1 = {'Email': 'hassan.abbas@cloudprimero.com',
                 'Password': 'PowerPoint@123'}
    userData2 = {'Email': 'ahassan.abbas@cloudprimero.com',
                 'Password': 'aPowerPoint@123'}
    requestId = None
    skipAll = False
    skipAllDummy = False
    failedTestCases = []


# it runs before everything else


@pytest.fixture(scope='function')
def driver(request):
    print("CURRENTWORKINGDIRECTORY :", os.getcwd())
    downloadsPath = os.getcwd() + '/Downloads/'
    if os.path.exists(downloadsPath):
        print("Path Exists : ", downloadsPath)
    else:
        print("Path Doesn't Exists:", downloadsPath)
        # os.mkdir(downloadsPath)
        print(os.path.exists(downloadsPath))
    print("FileDownloadDIRECTORY : ", downloadsPath)
    print(request.config.option.browser)
    BROWSER = request.config.option.browser
    driver = None

    if request.config.option.headless == "1":
        headless = "--headless=new"
    else:
        headless = "headfull"

    if BROWSER == "CHROME":
        chrome_options = Chrome_options()
        chrome_options.add_argument(headless)
        chrome_options.add_argument('--log-level=3')
        # chrome_options.add_argument("start-maximized")
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 1,
            "download.default_directory": downloadsPath,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing_for_trusted_sources_enabled": False,
            "safebrowsing.enabled": False,
            'behavior': 'allow'
        })
        # chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--disable-dev-shm-usage")
        # chrome_options.add_argument("--headless=new")
        # chrome_options.add_argument("window-size=1920,1080")
        # chrome_options.add_experimental_option("prefs", {
        #     "download.default_directory": downloadsPath,
        #     "download.prompt_for_download": False,
        #     "download.directory_upgrade": True,
        #     "safebrowsing.enabled": True,
        #     "DOWNLOADS_PATH": downloadsPath
        # })

        driver = webdriver.Chrome(
            ChromeDriverManager().install(), chrome_options=chrome_options)

    elif BROWSER == "FIREFOX":
        firefox_options = Firefox_options()
        # setup for downloadable files
        firefox_options.set_preference("browser.download.folderList", 2)
        firefox_options.set_preference(
            "browser.download.manager.showWhenStarting", False)
        firefox_options.set_preference("browser.download.dir", downloadsPath)
        firefox_options.set_preference(
            "browser.helperApps.neverAsk.saveToDisk", "application/pdf")

        firefox_options.add_argument(headless)
        firefox_options.add_argument('--log-level=3')
        firefox_options.add_argument("start-maximized")
        firefox_options.set_preference(
            'permissions.default.desktop-notification', 1)
        driver = webdriver.Firefox(service=Firefox_service(
            GeckoDriverManager().install()), options=firefox_options)
        # driver = webdriver.Firefox(GeckoDriverManager().install(), options=firefox_options)

    elif BROWSER == "OPERA":
        pass
        # driver = webdriver.Chrome(service=Service(
        #     ChromeDriverManager().install()))

    else:
        pytest.skip(allow_module_level=True,
                    reason="Please provide a browser name to initiate tests")

    driver.implicitly_wait(7)
    driver.set_window_size(1920, 1080)
    yield driver
    # sleep(180)
    driver.close()
    driver.quit()


# @pytest.fixture(scope='function', autouse=True)
# def clearDownloads():
#     yield
#     # Will be executed after the last test
#     downloadsPath = os.getcwd() + '/Downloads/'
#     files = os.listdir(downloadsPath)
#     # deleting all files in the downloads folder
#     for file_name in files:
#         file_path = os.path.join(downloadsPath, file_name)
#         try:
#             if os.path.isfile(file_path):
#                 os.remove(file_path)
#                 print(f"Deleted {file_path}")
#         except Exception as e:
#             print(f"Error deleting {file_path}: {e}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'driver' in item.fixturenames:
                    driver = item.funcargs['driver']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))

#  pytest --alluredir=reports  --browser CHROME --headless 0 -n 4 --reruns 2

# pytest Tests --alluredir=reports --screenshot=on --browser CHROME  -v -s --headless 0
# parallel test execution with 2 retry on failure
# Pytest Tests  --alluredir=reports --screenshot=on --browser CHROME  --headless 0 -n 10 --reruns 2
# pytest xdist
