# coding:utf-8

from selenium import webdriver
from common.BasePage import BasePage
from page.memberpage import MemberPage
import time


class huiyuan(BasePage, MemberPage):
    def click_inmember(self):
        '''进入会员管理页面'''
        self.click(self.huiyuan_guanli)

    def click_newmember(self):
        '''点击新增会员按钮'''
        self.click(self.huiyuan_xinzeng)

    def input_membername(self, membername):
        '''输入会员简称'''
        self.sendKeys(self.huiyuan_jianchen, membername)

    def input_phonenumber(self, phonenumber):
        '''输入手机号码'''
        self.sendKeys(self.huiyuan_shoujihao, phonenumber)

    def click_baocun(self):
        '''点击保存按钮'''
        self.click(self.huiyuan_btn_loc)

