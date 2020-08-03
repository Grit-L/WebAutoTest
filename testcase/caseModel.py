# -*- coding: utf-8 -*-
"""
@author: hanfeng.lin
@contact: wahaha
@Created on: 2020/7/27 15:12
"""
import unittest
import warnings

from webUIAtuo.common.driver import BrowserDriver
# from webUIAtuo.page.homePage import HomePage
from webUIAtuo.page.loginPage import LoginPage


class Model(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        driver = BrowserDriver(cls)
        cls.driver = driver.open_browser(cls)
        warnings.simplefilter("ignore", ResourceWarning)
        login = LoginPage(cls.driver)
        login.input_username_text('xuser')
        login.input_pwd_text('Zc123456')
        login.click_login_btn()

    def setup(self):
        pass

    def teardown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
