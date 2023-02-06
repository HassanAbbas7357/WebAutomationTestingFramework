import allure
import pytest
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_options
from selenium.webdriver.chrome.service import Service as Chrome_service
from selenium.webdriver.firefox.options import Options as Firefox_options
from selenium.webdriver.firefox.service import Service as Firefox_service


# from selenium.webdriver.opera.options import Options as Ooptions
# from selenium.webdriver.opera.service import Service as Oservice

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager
from selenium.webdriver.common.keys import Keys


@allure.step("finding the element")
def find_byXpath(xpath, driver):
    try:
        ele = driver.find_element(By.XPATH, xpath)
        print("Element Found with Xpath", xpath)
        return ele

    except:
        sleep(2)
        pytest.fail(
            f"Couldn't find element with selector with xpath : {xpath}")


@allure.step("finding the element")
def find_byXpathAndWait(xpath, driver):
    try:
        ele = WebDriverWait(driver, 7).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )

        print("Element Found with Xpath", xpath)
        return ele

    except:
        sleep(2)
        pytest.fail(
            f"Couldn't find element with selector with xpath : {xpath}")


@allure.step("finding the elements")
def find_Elements_byXpath(xpath, driver):
    try:
        ele = driver.find_elements(By.XPATH, xpath)
        print("Element Found with Xpath", xpath)
        if len(ele) == 0:
            pytest.fail(
                f"Couldn't find elements with selector with xpath : {xpath}")
        return ele

    except:
        pytest.fail(
            f"Couldn't find element with selector with xpath : {xpath}")
