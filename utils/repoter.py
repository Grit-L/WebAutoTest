# -*- coding: utf-8 -*-
"""
@author: hanfeng.lin
@contact: wahaha
@Created on: 2020/7/28 15:15
"""
import os
import time

# from webUIAtuo.report.HTMLTestRunner3 import HTMLTestRunner
from webUIAtuo.report.HTMLTestRunner import HTMLTestRunner
from webUIAtuo.utils.logger import Logger

logger = Logger(logger='Reporter').get_log()


class Reporter:
    PATH = os.getcwd() + '\\report\\testReporter\\' + time.strftime("%Y%m%d_%H%M%S_")

    @classmethod
    def generate_reporter(cls):
        logger.info('开始生成测试报告模板……')
        result_path = cls.PATH + 'test_result.html'
        try:
            fp = open(result_path, 'wb')
            runner = HTMLTestRunner(
                stream=fp,
                title='测试报告',
                description='测试用例执行情况'
            )
            logger.info('测试报告模板生成完成！')
            return fp, runner
        except Exception as e:
            logger.error('无法生成测试报告：%s' % e)





