# -*- coding: utf-8 -*-
"""
@author: hanfeng.lin
@contact: wahaha
@Created on: 2020/7/27 10:51
"""
import time

import yaml
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from webUIAtuo.utils.logger import Logger


logger = Logger(logger='BaseAction').get_log()


class BaseAction:
    def __init__(self, driver):
        self.driver = driver
        # 动态给各个页面locator赋值
        eles = yaml.load(open('./config/page_locator.yml').read())[self.__class__.__name__]
        for ele in eles:
            self.__setattr__(ele, eles[ele])

    def find_element(self, locator):
        """
        元素定位
        :param locator:
        :return:
        """
        try:
            return self.driver.find_element(*locator)  # 加*locator是为了解包
        except NoSuchElementException:
            logger.warning('找不到定位元素: %s' % locator[1])
            raise
        except TimeoutException:
            logger.warning('查找元素超时: %s' % locator[1])
            raise

    def send_key(self, locator, text):
        """
        文本框输入
        :param locator:
        :param text:
        :return:
        """
        logger.info('清空文本框内容: %s...' % locator[1])
        self.find_element(locator).clear()
        # time.sleep(1)
        logger.info('输入内容方式 by %s: %s...' % (locator[0], locator[1]))
        logger.info('输入内容: %s' % text)
        # self.log.myloggger('Input: %s' % text, flag=0)
        try:
            self.find_element(locator).send_keys(text)
            # time.sleep(2)
        except Exception as e:
            logger.error("输入内容失败 %s" % e)
            # self.get_screen_img(text)

    def click(self, locator):
        """
        点击操作
        :param locator:
        :return:
        """
        logger.info('点击元素 by %s: %s...' % (locator[0], locator[1]))
        try:
            self.find_element(locator).click()
            # time.sleep(2)
        except AttributeError as e:
            logger.error("无法点击元素: %s" % e)
            raise

    def swicth_to_frame(self, locator):
        """
        切换frame
        :param locator:
        :return:
        """
        logger.info('切换frame到: %s...' % locator)
        try:
            self.driver.switch_to.frame(locator)
        except Exception as e:
            logger.error("切换frame失败 %s" % e)

    def keyboard_action(self, locator, action):
        """
        键盘操作
        :param locator:
        :param action:
        :return:
        """
        ele = self.find_element(locator)
        try:
            if action in ['enter', 'Enter', 'ENTER']:
                logger.info('点击enter键 by %s: %s...' % (locator[0], locator[1]))
                ele.send_keys(Keys.ENTER)
            elif action in ['del', 'delete']:
                logger.info('点击delete键 by %s: %s...' % (locator[0], locator[1]))
                ele.send_keys(Keys.BACK_SPACE)
            elif action in ['space', 'Space']:
                logger.info('点击空格键 by %s: %s...' % (locator[0], locator[1]))
                ele.send_keys(Keys.BACK_SPACE)
            elif action in ['F']:
                logger.info('点击ctrl+F键 by %s: %s...' % (locator[0], locator[1]))
                ele.send_keys(Keys.CONTROL, 'f')
        except Exception as e:
            logger.error('键盘操作失败: %s' % e)

    def hover(self, locator):
        """
        鼠标悬停
        :param locator:
        :return:
        """
        ele = self.find_element(locator)
        ActionChains(self.driver).move_to_element(ele).perform()

    def get_screen_shot(self, value):
        """
        页面截图
        :return:
        """
        file_path = './report/screenshot/'
        now = time.strftime("%Y-%m-%d_%H_%M_%S")
        image_path = file_path + value + now + '.png'
        try:
            self.driver.get_screenshot_as_file(image_path)
            logger.info("页面已截图，图片：%s" % (value + now + '.png'))
        except NameError as ne:
            logger.error("失败截图 %s" % ne)
            self.get_screen_shot(value)
