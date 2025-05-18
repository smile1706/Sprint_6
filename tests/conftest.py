import pytest

from selenium import webdriver
from curl import *


@pytest.fixture(scope="function")
def driver():
    browser = webdriver.Firefox()
    browser.set_window_size(1600, 980)
    browser.get(main_site)
    yield browser
    browser.quit()

