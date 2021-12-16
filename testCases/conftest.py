import pytest
from selenium import webdriver

@pytest.fixture
def setup():
    driver=webdriver.Chrome(executable_path="c:\selenium\chromedriver.exe")
    return driver