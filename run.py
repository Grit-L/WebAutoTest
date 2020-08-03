# -*- coding: utf-8 -*-
"""
@author: hanfeng.lin
@contact: wahaha
@Created on: 2020/7/27 11:08
"""
from webUIAtuo.utils.caseSuite import CaseSuite
from webUIAtuo.utils.emailer import SendEmail
from webUIAtuo.utils.repoter import Reporter


def run():
    test_suite = CaseSuite.create_suite()
    fp, runner = Reporter.generate_reporter()
    runner.run(test_suite, rerun=0, save_last_run=False)
    fp.close()
    SendEmail.mail_email()


if __name__ == '__main__':
    run()
