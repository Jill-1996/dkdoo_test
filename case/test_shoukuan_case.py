# coding:utf-8

from selenium import webdriver
from page.loginpage import LoginPage
from page.memberpage import MemberPage
# from page.member_one import huiyuan
from page.shoukuankaikapage import ShoukuanPage
# from page.shoukuankaika import shoukuankaika
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time


class ShoukuanCase(unittest.TestCase):
    driver = None

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.log = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.login = LoginPage(cls.driver)
        cls.huiyuan = MemberPage(cls.driver)
        # cls.huiyuan1 = huiyuan(cls.driver)
        cls.money = ShoukuanPage(cls.driver)
        # cls.shoukuan1 = shoukuankaika(cls.driver)

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
        '''输入正确的账号密码登录'''
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

    # def test_02(self):
    #     '''进入会员管理菜单主页'''
    #     self.money.click_inmember()
    #     '''点击新增会员按钮'''
    #     self.money.click_newmember()
    #     '''输入会员简称'''
    #     self.money.input_membername("test001")
    #     '''输入会员手机号码'''
    #     self.money.input_phonenumber("010123134564897")
    #     '''点击保存按钮'''
    #     self.money.click_baocun()

    def test_03(self):
        '''点击收款菜单'''
        self.money.click_shoukuan()
        '''点击搜索框'''
        self.money.click_sousuokuang()
        '''点击下拉框第一个会员'''
        self.money.click_onemember()
        time.sleep(2)

    def test_04(self):
        '''进入收款主页-收款/开卡-选择第一个服务'''
        self.money.click_chooseservice()
        time.sleep(2)
        '''点击选择现金支付'''
        # self.money.click_cash()
        self.money.input_cash("100")
        time.sleep(2)
        '''点击确定支付'''
        self.money.click_queding()
        '''二次确认支付'''
        self.money.click_surequeding()
        time.sleep(2)

    # def tearDown(self):
    #     self.driver.delete_all_cookies() # 清空cookies
    #     self.driver.refresh()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main