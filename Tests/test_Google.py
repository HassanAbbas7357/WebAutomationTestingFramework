from conftest import *
from base_helpers import *


def test_visitSite(driver):
    driver.get("https://google.com")
    find_byXpath("//button[@id=submit]", driver).click()
