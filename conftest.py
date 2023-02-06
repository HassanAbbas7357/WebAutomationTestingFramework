import pytest
from pytest import fixture
from conftest import *
from base_helpers import *


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
    )
    parser.addoption(
        "--headless", action="store", default="input2"
    )


class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


class Storage:
    userData1 = None
    userData2 = None
    requestId = None
    skipAll = False
    skipAllDummy = False
    failedTestCases = []


@pytest.fixture(scope='session')
def driver(request):
    print(request.config.option.browser)
    BROWSER = request.config.option.browser

    headless = ""

    if request.config.option.headless == "1":
        headless = "--headless"
    else:
        headless = "headfull"

    if BROWSER == "CHROME":
        chrome_options = Chrome_options()
        chrome_options.add_argument(headless)
        chrome_options.add_argument('--log-level=3')
        chrome_options.add_argument("start-maximized")
        chrome_options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 1
        })

        driver = webdriver.Chrome(service=Chrome_service(
            ChromeDriverManager().install()), options=chrome_options)

    elif BROWSER == "FIREFOX":
        firefox_options = Firefox_options()
        firefox_options.add_argument(headless)
        firefox_options.add_argument('--log-level=3')
        firefox_options.add_argument("start-maximized")
        firefox_options.set_preference(
            'permissions.default.desktop-notification', 1)
        driver = webdriver.Firefox(service=Firefox_service(
            GeckoDriverManager().install()), options=firefox_options)

    elif BROWSER == "OPERA":
        pass
        # driver = webdriver.Chrome(service=Service(
        #     ChromeDriverManager().install()))

    else:
        pytest.skip(allow_module_level=True,
                    reason="Please provide a browser name to innitiate tests")

    driver.implicitly_wait(7)
    driver.maximize_window()
    yield driver
    # sleep(180)
    driver.close()
    driver.quit()
