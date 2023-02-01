# coding:utf-8

from common.BasePage import BasePage
from page.memberpage import MemberPage
from page.shoukuankaikapage import ShoukuanPage
from page.memberone import huiyuan
import time


class shoukuankaika(BasePage, ShoukuanPage):

    def click_shoukuan(self):
        '''点击收款菜单'''
        self.click(self.Shoukuan_loc)
        time.sleep(0.5)

    def click_sousuokuang(self):
        '''点击搜索框'''
        self.click(self.search_loc)
        time.sleep(0.5)

    def click_onemember(self):
        '''选择下拉框第一个会员'''
        self.click(self.onemember)
        time.sleep(0.5)

    # '''
    # 收款-新增会员
    # '''
    # def click_huiyuanguanli(self):
    #     '''点击会员管理菜单'''
    #     self.click(self.huiyuan_guanli)
    #
    # def click_huiyuan(self):
    #     '''点击新增会员'''
    #     self.click(self.huiyuan_xinzeng)
    #     time.sleep(0.5)
    #
    # def input_member_jiancheng(self, name):
    #     '''点击输入会员简称'''
    #     self.sendKeys(self.member_jiancheng, name)
    #
    # def input_member_leixing(self, leixing):
    #     '''点击输入会员类型'''
    #     self.sendKeys(self.member_leixing, leixing)
    #
    # def input_member_yingwenming(self, yingwenming):
    #     '''点击输入会员英文名'''
    #     self.sendKeys(self.huiyuan_yingwenming, yingwenming)
    #
    # def input_member_mingcheng(self, mingcheng):
    #     '''点击输入会员名称'''
    #     self.sendKeys(self.huiyuan_mingcheng, mingcheng)
    #
    # def input_member_shoujihao(self, phone):
    #     '''点击输入会员手机号'''
    #     self.sendKeys(self.huiyuan_shoujihao, phone)
    #
    # def input_member_shenfenzheng(self, shenfenzheng):
    #     '''点击输入会员身份证号'''
    #     self.sendKeys(self.huiyuan_shenfenzheng, shenfenzheng)
    #
    # def click_cancel(self):
    #     '''点击取消按钮'''
    #     self.click(self.huiyuan_btn_normal_loc)
    #
    # def click_save(self):
    #     '''点击保存按钮'''
    #     self.click(self.huiyuan_btn_loc)

    '''
    收款-选择收款/开卡tab-服务tab
    '''
    def click_choosefuwu(self):
        '''点击进入收款/开卡tab'''
        self.click(self.shoukuan_kaika)

    def click_chooseservice(self):
        '''点击选择第一个服务'''
        self.click(self.shoukuan_fuwu_one)

    '''
    收款-销售单右侧
    '''
    def input_cash(self, cash):
        '''现金支付'''
        self.sendKeys(self.shoukuan_Cash, cash)

    def click_queding(self):
        '''确定支付'''
        self.click(self.shoukuan_quedingzhifu)

    def click_surequeding(self):
        '''二次确定'''
        self.click(self.shoukuan_sure_queding)