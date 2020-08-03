# -*- coding: utf-8 -*-
"""
@author: hanfeng.lin
@contact: wahaha
@Created on: 2020/7/28 15:17
"""
import email
import smtplib
import email.mime.multipart
import email.mime.text
from email.header import Header
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

from webUIAtuo.config import config
from webUIAtuo.utils.logger import Logger

logger = Logger(logger='Email').get_log()


class SendEmail:

    @classmethod
    def mail_email(cls):
        # 网易邮箱
        # 请自行修改下面的邮件发送者和接收者
        logger.info('开始发送邮件……')
        sender = config.SENDER
        receivers = config.RECEIVERS
        c_receivers = config.C_RECEIVERS
        content = config.CONTENT
        '''
        必填，不然会报504错误
        From ：发送的邮箱账号
        to： 接收的邮箱账号
        '''

        message = email.mime.multipart.MIMEMultipart()
        message['from'] = sender
        message['to'] = ','.join(receivers)
        message['cc'] = ','.join(c_receivers)
        message['subject'] = config.SUBJECT
        content = content
        txt = email.mime.text.MIMEText(content, 'plain', 'utf-8')
        message.attach(txt)

        # 添加附件地址
        part = MIMEApplication(open(config.ACCESSORY_PATH, 'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename=config.ACCESSORY_NAME)  # 发送文件名称
        message.attach(part)

        smtper = smtplib.SMTP('smtp.163.com')
        # smtper.connect(smtpHost, '25')
        smtper.login(sender, config.SMTP_PASSWORD)
        smtper.sendmail(sender, receivers, message.as_string())
        logger.info('邮件发送成功！')
        smtper.quit()

    @classmethod
    def qq_email(cls):
        # qq邮箱
        sender = config.SENDER
        receivers = config.RECEIVERS
        c_receivers = config.C_RECEIVERS
        content = config.CONTENT
        '''
        必填，不然会报504错误
        From ：发送的邮箱账号
        to： 接收的邮箱账号
        '''
        message = email.mime.multipart.MIMEMultipart()
        message['from'] = sender
        message['to'] = ','.join(receivers)
        message['cc'] = ','.join(c_receivers)
        message['subject'] = config.SUBJECT
        content = content
        txt = email.mime.text.MIMEText(content, 'plain', 'utf-8')
        message.attach(txt)

        # 添加附件地址
        part = MIMEApplication(open(config.ACCESSORY_PATH, 'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename=config.ACCESSORY_NAME)  # 发送文件名称
        message.attach(part)

        # 发送端服务器，这里是qq的服务器
        smtper = smtplib.SMTP('smtp.qq.com')
        # 登录账号和授权码，不是密码是授权码
        smtper.login(sender, 'xxxxxx')
        smtper.sendmail(sender, receivers, message.as_string())
        print('邮件发送完成!')
        smtper.quit()

    @classmethod
    def outlook(cls):
        # outlook邮箱
        pass


if __name__ == '__main__':
    s = SendEmail()
    s.mail_email()
