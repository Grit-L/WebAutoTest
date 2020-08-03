# -*- coding: utf-8 -*-
"""
@author: hanfeng.lin
@contact: wahaha
@Created on: 2020/7/27 15:16
"""
import time


from webUIAtuo.page.homePage import HomePage
from webUIAtuo.testcase.caseModel import Model


class Case(Model):

    def test_login(self):
        assert self.driver.title == '神州专车后台管理系统'
        # self.assertEqual(self.driver.title, '神州专车后台管理系统', msg='断言错误')

    def test_home(self):
        home_page = HomePage(self.driver)
        home_page.click_search()
        home_page.input_search('呼叫中心管理')
        home_page.move_to_result()
        home_page.click_search_btn()
        home_page.get_screen_shot('首页')
        time.sleep(5)


# if __name__ == '__main__':
# #     unittest.main()
