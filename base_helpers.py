import os.path
import pandas as pd
import allure
import pytest
from time import sleep
import time
from random import randrange
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException, \
    ElementNotInteractableException, ElementNotVisibleException
import random
import string
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
from Locators.TempWorkersLocators import TableRow_xpath, TextRow_xpath

waitTimer = 15
LoaderWaitTimer = 25


def get_randomEmail():
    return ''.join(random.choice(string.ascii_letters) for _ in range(15)) + "1421@gmail.com"


def press_Enter(driver):
    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER)
    actions.perform()


def find_byXpath(xpath, driver):
    try:
        ele = driver.find_element(By.XPATH, xpath)
        print("Element Found with Xpath", xpath)
        return ele
    except NoSuchElementException:
        pytest.fail(
            f"Couldn't find element with xpath : {xpath}")


def find_byXpathAndGet_text(xpath, driver):
    try:
        ele = driver.find_element(By.XPATH, xpath)
        print("Element Found with Xpath", xpath)
        return ele.text
    except NoSuchElementException:
        pytest.fail(
            f"Couldn't find element with xpath : {xpath}")


def click_on_element_js(xpath, driver):
    try:
        find_byXpath(xpath, driver).click()
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].click();", find_byXpath(xpath, driver))


def find_byXpathAndWait(xpath, driver):
    try:
        ele = WebDriverWait(driver, waitTimer).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )

        print("Element Found with Xpath", xpath)
        return ele

    except (NoSuchElementException, TimeoutException):
        pytest.fail(
            f"Couldn't find element with xpath : {xpath}")


def find_Elements_byXpathAndWait(xpath, driver):
    try:
        ele = WebDriverWait(driver, waitTimer).until(
            EC.presence_of_all_elements_located((By.XPATH, xpath))
        )
        if len(ele) == 0:
            pytest.fail(
                f"Couldn't find elements with xpath : {xpath}")

        print("Elements Found with Xpath", xpath)
        return ele

    except (NoSuchElementException, TimeoutException):
        pytest.fail(
            f"Couldn't find element with xpath : {xpath}")


def find_Elements_byXpathAndWait_getText(xpath, driver):
    sleep(2)
    return list((i.text for i in find_Elements_byXpathAndWait(xpath, driver)))


def find_Elements_byXpath(xpath, driver):
    try:
        ele = driver.find_elements(By.XPATH, xpath)
        print("Elements Found with Xpath", xpath)
        if len(ele) == 0:
            pytest.fail(
                f"Couldn't find elements with xpath : {xpath} list has length 0")
        return ele

    except:
        pytest.fail(
            f"Couldn't find elements with xpath : {xpath}")


def check_IFRedirectedON_ValidUrl(expectedUrl, driver):
    assert expectedUrl == driver.current_url


def visitUrl(url, driver):
    driver.get(url)


def verify_visibility_of_element_located(xpath, driver):
    try:
        WebDriverWait(driver, waitTimer).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    except (ElementNotVisibleException, TimeoutException):
        pytest.fail(
            f"Element not visible with xpath : {xpath}")


def verify_elementIsClickAble(xpath, driver):
    try:
        WebDriverWait(driver, waitTimer).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    except (ElementNotInteractableException, TimeoutException):
        pytest.fail(
            f"Element not visible with xpath : {xpath}")


def verify_loaderAndWait(xpath, driver):
    print('waiting for loader to disappear')
    while True:
        try:
            driver.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            break
    print('loader disappeared')


def verify_element_is_present(xpath, driver):
    try:
        find_byXpathAndWait(xpath, driver)
    except NoSuchElementException:
        pytest.fail(
            f"Couldn't find element with xpath : {xpath}")
    try:
        scroll_into_element(xpath, driver)
        find_byXpathAndWait(xpath, driver).is_displayed()
    except ElementNotVisibleException:
        pytest.fail(
            f"Element with xpath : {xpath} is not visible")


def scroll_into_element(xpath, driver):
    """find element by xpath and scroll to that element"""
    element = None
    try:
        element = find_byXpath(xpath, driver)
    except NoSuchElementException:
        pytest.fail(
            f"Couldn't find element with xpath : {xpath}")
    if element is not None:
        print('scrolling to', xpath)
        driver.execute_script("arguments[0].scrollIntoView();", element)
    else:
        pytest.fail(
            f"Couldn't Scroll into element with xpath : {xpath}")


# def verify_Data_TableCell(driver, xpathAtrr):
#     NameXpath = TableRow_xpath(xpathAtrr)
#     assert find_byXpathAndGet_text(NameXpath, driver) == xpathAtrr
#     print(f'Date Found {xpathAtrr}')

def replace_string(input_string):
    if ", " in input_string:
        return input_string.replace(", ", " (") + ")"
    else:
        return input_string


def verify_Data_TableCell(driver, listxpathAtrr, tableIndex=0):
    for xpathAtrr in listxpathAtrr:
        NameXpath = TableRow_xpath(xpathAtrr, tableIndex)
        print(NameXpath)
        assert find_byXpathAndGet_text(NameXpath, driver) == xpathAtrr
        print(f'Data Found {xpathAtrr}')


def verify_Data_TableCell_ByTextXpath(driver, listxpathAtrr, tableIndex=0):
    for xpathAtrr in listxpathAtrr:
        NameXpath = TextRow_xpath(xpathAtrr, tableIndex)
        assert find_byXpathAndGet_text(NameXpath, driver) == xpathAtrr
        print(f'Data Found {xpathAtrr}')


def scroll_to_top_of_page(driver):
    driver.execute_script(
        "window.scrollTo(document.body.scrollHeight, 0)")


def scroll_to_bottom_of_page(driver):
    actions = ActionChains(driver)
    actions.move_to_element(driver.find_element(By.TAG_NAME, 'body')).click().perform()
    actions.key_down(Keys.CONTROL).send_keys(Keys.END).key_up(Keys.CONTROL).perform()


def verifyFileDownloadedCorrectly(FilePath):
    assert os.path.exists(FilePath)

# --------------------------------------


# def wait_for_element_visibility(self, locator, timeout=10):
#     return (
#         WebDriverWait(self.driver, timeout)
#         .until(
#             EC.visibility_of_element_located(
#                 get_locator(self.driver, locator, timeout)
#             )
#         )
#     )


# def wait_for_element_clickable(self, locator, timeout=10):
#     return (
#         WebDriverWait(self.driver, timeout)
#         .until(
#             EC.element_to_be_clickable(
#                 get_element(self.driver, locator, timeout)
#             )
#         )
#     )


# def get_element_attribute(self, locator, attribute, timeout=10):
#     if type(locator) == list:
#         element = get_element(self.driver, locator, timeout)
#     else:
#         element = locator
#     return (
#         element.get_attribute(attribute)
#     )


# def verify_all_elements_are_present(self, locator, timeout=10):
#     return WebDriverWait(self.driver, timeout).until(
#         EC.presence_of_all_elements_located(
#             locator[app][0], locator[app][1]
#         )
#     ).is_displayed()


# def verify_element_with_specific_text_is_present(self, text, timeout=10):
#     locator = '//*[contains(text(),"{placeholder}")]'.replace(
#         "{placeholder}", text)
#     return WebDriverWait(self.driver, timeout).until(
#         EC.presence_of_element_located(
#             (By.XPATH, locator)
#         )
#     ).is_displayed()


# def click_on_element(self, locator, timeout=10):
#     if type(locator) == list:
#         element = get_element(self.driver, locator, timeout)
#     else:
#         element = locator
#     element.click()


# def from_list_click_on_random_element(self, locator, timeout=10):
#     elements = get_elements(self.driver, locator, timeout)
#     time.sleep(1)
#     elements[randrange(len(elements))].click()


# def from_list_click_on_element_on_specific_index(self, locator, index, timeout=10):
#     elements = get_elements(self.driver, locator, timeout)
#     elements[index].click()


# def from_list_click_on_first_element(self, locator, timeout=10):
#     elements = get_elements(self.driver, locator, timeout)
#     elements[0].click()


# def from_list_get_elements_size(self, locator, timeout=10):
#     elements = get_elements(self.driver, locator, timeout)
#     return len(elements)


# def from_list_click_on_element_js(self, locator, timeout=10):
#     self.driver.execute_script("arguments[0].click();", get_elements(
#         self.driver, locator, timeout)[0])


# def from_list_click_on_valid_element_js(self, locator, timeout=10):
#     elements = get_elements(self.driver, locator, timeout)
#     for element in elements:
#         try:
#             self.driver.execute_script("arguments[0].click();", element)
#         except:
#             pass


# def from_list_click_on_valid_element(self, locator, timeout=10):
#     elements = get_elements(self.driver, locator, timeout)
#     for element in elements:
#         try:
#             element.click()
#         except:
#             pass


# def element_is_displayed(self, locator, timeout=10):
#     return get_element(self.driver, locator, timeout).is_displayed()


# def send_keys_to_element(self, locator, input_value, timeout=10):
#     if type(locator) == list:
#         element = get_element(self.driver, locator, timeout)
#     else:
#         element = locator
#     element.clear()
#     element.click()
#     ActionChains(self.driver).move_to_element(element).click().key_down(
#         Keys.CONTROL
#     ).send_keys("a").key_up(Keys.CONTROL).send_keys(input_value).perform()


# def send_key(self, locator, Key, timeout=10):
#     get_element(self.driver, locator, timeout).send_keys(Key)


# def get_text_of_an_element(self, locator, timeout=10):
#     if type(locator) == list:
#         element = get_element(self.driver, locator, timeout)
#     else:
#         element = locator
#     return element.text


# def switch_to_default(self):
#     self.driver.switch_to.default_content()


# def switch_window(self):
#     curr_win = self.driver.current_window_handle
#     tabs = self.driver.window_handles
#     for tab in tabs:
#         if tab != curr_win:
#             self.driver.switch_to.window(tab)


# def switch_tab_by_title(self, title):
#     for tab in self.driver.window_handles:
#         if tab != self.driver.current_window_handle:
#             self.driver.switch_to.window(tab)
#             if self.driver.title == title or title in self.driver.title:
#                 break


# def open_tab(self):
#     self.driver.execute_script("window.open('');")


# def close_tab(self):
#     self.driver.close()
#     self.driver.switch_to.window(self.driver.window_handles[0])


# def switch_tab(self):
#     for tab in self.driver.window_handles:
#         self.driver.switch_to.window(tab)
#         if self.driver.title != "Spekit Sidebar":
#             self.driver.close()
#     self.driver.switch_to.window(self.driver.window_handles[0])


# def get_current_url(self):
#     return self.driver.current_url


# def open_spekit_url(self):
#     url = settings.BASE_URL
#     self.driver.get(url)


# def refresh_tab(self):
#     self.driver.refresh()
#     time.sleep(2)


# def open_url(self, url):
#     self.driver.get(url)


# def wait_for_page_load(self, desired_url):
#     try:
#         WebDriverWait(self.driver, 30).until(
#             lambda driver: driver.current_url == desired_url
#         )
#     except ValueError as e:
#         print("Another URL has been displayed i.e. " + str(e))


# def switch_to_default(self):
#     self.driver.switch_to.default_content()
#     time.sleep(2)


# def switch_to_iframe(self, locator, timeout=10):
#     switch_to_default(self)
#     spek_modal = self.driver.find_element_by_css_selector(locator)
#     self.driver.switch_to.frame(spek_modal)


# def hover_on_element(self, locator, timeout=10):
#     if type(locator) == list:
#         element = get_element(self.driver, locator, timeout)
#     else:
#         element = locator
#     time.sleep(1.5)
#     action = ActionChains(self.driver)
#     action.move_to_element(element).perform()
