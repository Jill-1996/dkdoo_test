# coding:utf-8

from selenium import webdriver
from page.loginpage import LoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import unittest
import time


class LoginCase(unittest.TestCase):
    driver = None

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.log = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.login = LoginPage(cls.driver)

    def setUp(self) -> None:
        self.driver.maximize_window()

    def login_case(self, username, psw):
        # 登录
        self.login.login(username, psw)
        # 判断是否有弹窗
        self.login.is_alert_exsit()
        # 获取结果
        result = self.login.get_login_result()
        return result

    def test_01(self):
        '''输入错误的账号密码登录'''
        # self.login.login()
        self.login.open_login_page()
        self.login.input_phoneNo("123456")
        self.login.input_password("123456")
        time.sleep(0.5)
        self.login.click_login_button()
        time.sleep(5)
        result = self.login.get_login_tishi1 or self.login.denglushibai2_loc()
        print("获取实际结果：%s" % result)
        return result

    def test_02(self):
        '''输入正确的账号,错误的密码登录'''
        # self.login.login()
        self.login.open_login_page()
        self.login.input_phoneNo("15012345678")
        self.login.input_password("123456")
        time.sleep(0.5)
        self.login.click_login_button()
        time.sleep(5)
        result = self.login.get_login_tishi1 or self.login.denglushibai2_loc()
        print("获取实际结果：%s" % result)
        return result

    def test_03(self):
        '''输入错误的账号,正确的密码登录'''
        # self.login.login()
        self.login.open_login_page()
        self.login.input_phoneNo("123456")
        self.login.input_password("dkd123456")
        time.sleep(0.5)
        self.login.click_login_button()
        time.sleep(5)
        result = self.login.get_login_tishi1 or self.login.denglushibai2_loc()
        print("获取实际结果：%s" % result)
        return result

    def test_04(self):
        '''输入正确的账号密码登录'''
        # self.log.info("------登录成功用例：start!---------")
        # self.login.login()
        self.login.open_login_page()
        self.login.input_phoneNo("15012345678")
        self.login.input_password("dkd123456")
        time.sleep(0.5)
        self.login.click_login_button()
        time.sleep(5)
        result = self.login.get_login_tishi3()
        print("获取实际结果：%s" % result)
        return result

    def tearDown(self):
        self.driver.delete_all_cookies() # 清空cookies
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main
