# -*- coding: utf-8 -*-
"""
@author: hanfeng.lin
@contact: wahaha
@Created on: 2020/7/28 15:14
"""
import unittest


class CaseSuite:
    @classmethod
    def create_suite(cls):
        test_suite = unittest.TestSuite()  # 测试集
        test_dir = './testcase'
        # print(test_dir)

        discover = unittest.defaultTestLoader.discover(
            start_dir=test_dir,
            pattern='test.py',
            top_level_dir=None
        )
        # print(discover)
        for test_case in discover:
            test_suite.addTests(test_case)
        return test_suite
