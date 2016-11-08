import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('-dr', action='store')


@pytest.fixture(scope='session')
def driver(request):
    par = request.config.getoption('--dr').lower()
    if par == 'firefox':
        desired_caps = {'browserName': 'firefox'}
        _driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=desired_caps)
    elif par == 'chrome':
        desired_caps = {"browserName": "chrome"}
        # desired_caps["platform"] = "LINUX"
        _driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=desired_caps)
    elif par == "ie":
        desired_caps = {'browserName': "internet explorer"}
        _driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=desired_caps)
    else:
        desired_caps = {'browserName': "chrome"}
        _driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=desired_caps)
    request.addfinalizer(_driver.quit)
    return _driver
