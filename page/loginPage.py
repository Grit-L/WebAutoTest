# -*- coding: utf-8 -*-
"""
@author: hanfeng.lin
@contact: wahaha
@Created on: 2020/7/27 10:43
"""

from webUIAtuo.common.baseAction import BaseAction
from webUIAtuo.page.homePage import HomePage


class LoginPage(BaseAction):

    def input_username_text(self, text):
        self.send_key(self._username_locator, text)

    def input_pwd_text(self, text):
        self.send_key(self._password_locator, text)

    def click_login_btn(self):
        self.click(self._login_locator)
        return HomePage(BaseAction)
