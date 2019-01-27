# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_hsgtcgNorthMoney
   Description : 测试北向持股
   Author :       pchaos
   date：          18-12-16
-------------------------------------------------
   Change Activity:
                   18-12-16:
-------------------------------------------------
"""
__author__ = 'pchaos'

import unittest, time, re
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

from stocks.tools.hsgtcgNorthMoney import HSGTCGNorthMoney


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        self.hm = HSGTCGNorthMoney("http://data.eastmoney.com/hsgtcg/StockStatistics.aspx")
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app_dynamics_job(self):
        # 测试北向资金大于minimumHoldAmount（5000）万
        hm = self.hm
        # minimumHoldAmount = 5000
        minimumHoldAmount = 3000
        hm.minimumHoldAmount = minimumHoldAmount
        # hm.prepareEnv('2018-11-26')
        # hm.prepareEnv('2018-12-1')
        # hm.prepareEnv('2018-12-8')
        hm.prepareEnv()
        totalpage, df = hm.getData()
        print(df)
        print('总页数：{}'.format(totalpage))
        print('股票市值小于{}万：\n{}'.format(minimumHoldAmount, df[df['hamount'] < minimumHoldAmount]))
        #
        self.assertTrue(50 * totalpage >= len(df) >= 50 * (totalpage - 1),
                        '总页数：{}, 返回数据长度：{}'.format(totalpage, len(df)))

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
