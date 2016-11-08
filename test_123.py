from time import sleep
import json
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

with open('codex.json') as data_file:
    data = json.load(data_file)


def _scroll_to_element(driver, ele):
    h = driver.get_window_size()
    driver.execute_script("return arguments[0].scrollIntoView();", ele)
    driver.execute_script("window.scrollBy(0, -" + str(h['height']/2) + ");")
    return driver


def _move_click(driver, xpath):
    ele = driver.find_element_by_xpath(xpath)
    _scroll_to_element(driver, ele)
    ele.click()
    sleep(3)
    return driver


def _wait(driver, xpath):
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath)))
    ele = driver.find_element_by_xpath(xpath)
    _scroll_to_element(driver, ele)


def _startup(driver):
    _base_url = "https://www.surveymonkey.com/user/sign-in/"
    driver.implicitly_wait(30)
    driver.get(_base_url)
    return driver


@pytest.fixture(scope='session')
def login(driver):
    _base_url = "https://www.surveymonkey.com/user/sign-in/"
    driver.implicitly_wait(30)
    driver.get(_base_url)
    driver.find_element_by_xpath(data['signInUsername']).send_keys('InfoBeans@Pune')
    driver.find_element_by_xpath(data['signInPassword']).send_keys('InfoBeans!@#')
    _move_click(driver, data['signInButton'])
    sleep(3)
    return driver

@pytest.fixture
def surveycreate(driver):
    _wait(driver, "//a[contains(@href, '/create/?ut_source=create_survey&ut_source2=header')]")
    _move_click(driver, "//a[contains(@href, '/create/?ut_source=create_survey&ut_source2=header')]")
    _wait(driver, "//input[@id='newName']")
    t1 = driver.find_element_by_xpath("//input[@id='newName']")
    t1.send_keys("HELP US")
    select = Select(driver.find_element_by_xpath('.//select[@id="newCategory"]'))
    select.select_by_value('6')
    _move_click(driver, '(.//a[@class="s1continue btn teal next"])[1]')
    return driver