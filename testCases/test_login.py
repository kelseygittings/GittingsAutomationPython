import os
import pytest
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pageObjects.LoginPage import LoginPage
from time import sleep

class Test_001_Login:
    loginURL = "https://hudl.com/login"
    username = os.environ.get('HUDL_USERNAME')
    password = os.environ.get('HUDL_PASSWORD')
    randomUsername = "random@random.com"
    randomPassword = "r@nd0mPa$$"

    #Successful Login
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.loginURL)
        self.driver.maximize_window()
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        homeURL = self.driver.current_url
        assert "https://www.hudl.com/home", homeURL
        self.driver.close()

    #Login using Tab to get to password and Enter to Login
    def test_loginWithTabAndEnter(self, setup):
        self.driver = setup
        self.driver.get(self.loginURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username).send_keys(Keys.TAB)
        self.lp.setPassword(self.password).send_keys(Keys.ENTER)
        homeURL = self.driver.current_url
        assert "https://www.hudl.com/home", homeURL
        self.driver.close()

    def test_loginWithWrongUsername(self, setup):
        self.driver = setup
        self.driver.get(self.loginURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.randomUsername)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        assert "We didn't recognize that email and/or password. ", self.driver.page_source
        self.driver.close()

    def test_loginWithWrongPassword(self, setup):
        self.driver = setup
        self.driver.get(self.loginURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.randomPassword)
        self.lp.clickLogin()
        assert "We didn't recognize that email and/or password. ", self.driver.page_source
        self.driver.close()

    def test_loginNoUsername(self, setup):
        self.driver = setup
        self.driver.get(self.loginURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setPassword(self.randomPassword)
        self.lp.clickLogin()
        assert "We didn't recognize that email and/or password. ", self.driver.page_source
        self.driver.close()

    def test_loginNoPassword(self, setup):
        self.driver = setup
        self.driver.get(self.loginURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.clickLogin()
        assert "We didn't recognize that email and/or password. ", self.driver.page_source
        self.driver.close()

    def test_loginOnlyClickLogin(self, setup):
        self.driver = setup
        self.driver.get(self.loginURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.clickLogin()
        assert "We didn't recognize that email and/or password. ", self.driver.page_source
        self.driver.close()

    def test_clickRememberMe(self, setup):
        self.driver = setup
        self.driver.get(self.loginURL)
        self.driver.maximize_window()
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickRememberMe()
        self.lp.clickLogin()
        homeURL = self.driver.current_url
        assert "https://www.hudl.com/home", homeURL
        self.driver.close()

    def test_loginNeedHelp(self, setup):
        self.driver = setup
        self.driver.get(self.loginURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.clickLogin()
        self.lp.clickNeedHelplink()
        assert "Login Help", self.driver.page_source
        self.driver.close()

    def tearDown(self):
        self.driver.quit()