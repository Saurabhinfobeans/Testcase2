import test_123
from selenium.common.exceptions import NoSuchElementException

login = test_123.login
sCreate = test_123.surveycreate


def test_login1(driver, login):
    try:
        driver.find_element_by_xpath('.//*[contains(text(), "Sign Out")]')
        so = 1
    except NoSuchElementException:
        try:
            driver.find_element_by_xpath('.//*[contains(text(), "Log Out")]')
            so = 1
        except NoSuchElementException:
            so = 0
    assert so != 0


def test_login2(driver, login):
    try:
        driver.find_element_by_xpath('.//*[contains(text(), "InfoBeans@Pune")]')
        so = 1
    except NoSuchElementException:
        so = 0
    assert so != 0


# def test_sCreate(driver, sCreate):
#     title = driver.find_element_by_xpath('.//span[@class="title-text"]').text
#     assert title == "HELP US"


