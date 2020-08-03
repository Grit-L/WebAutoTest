# -*- coding: utf-8 -*-
"""
@author: hanfeng.lin
@contact: wahaha
@Created on: 2020/7/27 14:36
"""
from selenium import webdriver

from webUIAtuo.config import config


class BrowserDriver:
    def __init__(self, driver):
        self.driver = driver
        self.url = config.URL
        self.driver_path = config.DRIVER_PATH

    def open_browser(self, driver: webdriver):
        driver = webdriver.Chrome(self.driver_path)
        driver.get(self.url)
        driver.implicitly_wait(10)
        return driver
