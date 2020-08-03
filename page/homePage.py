# -*- coding: utf-8 -*-
"""
@author: hanfeng.lin
@contact: wahaha
@Created on: 2020/7/27 11:04
"""

from webUIAtuo.common.baseAction import BaseAction


class HomePage(BaseAction):

    def click_search(self):
        self.swicth_to_frame(self._frame_name_locator)
        self.click(self._search_locator)

    def input_search(self, text):
        self.send_key(self._search_input_locator, text)

    def move_to_result(self):
        self.hover(self._search_result_locator)

    def click_search_btn(self):
        self.click(self._search_result_locator)

