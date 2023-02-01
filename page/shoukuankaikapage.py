# coding:utf-8

from common.BasePage import BasePage
from page.memberpage import MemberPage
import time


class ShoukuanPage():
    # 收款-主页
    Shoukuan_loc = ("xpath", '//span[@class="menu-nav iconfont icon-payment"]/../span[2]')  # 收款菜单
    search_loc = ("xpath", '//article[@class="charge-v2 flex"]/header/div/div/charge-member-select-v2/div/div/input')  # 点击搜索框
    onemember = ("id", "62e733fce4b02279a11e641c")  # 点击下拉框第一个会员

    # 收款所有tab
    shoukuan_kouka = ("xpath", '//section[@class="charge-nav ng-scope"]/div/div[2]/ul/li[1]/a') # 点击扣次卡
    shoukuan_kaika = ("xpath", '//section[@class="charge-nav ng-scope"]/div/div[2]/ul/li[2]/a')  # 点击收款/开卡
    shoukuan_gouchuzhika = ("xpath", '//section[@class="charge-nav ng-scope"]/div/div[2]/ul/li[3]/a')  # 点击购储值卡
    shoukuan_chongchuzhika = ("xpath", '//section[@class="charge-nav ng-scope"]/div/div[2]/ul/li[4]/a')  # 点击充储值卡
    shoukuan_tuikatuishangpin = ("xpath", '//section[@class="charge-nav ng-scope"]/div/div[2]/ul/li[5]/a')  # 点击退卡/退商品
    shoukuan_taocantihuan = ("xpath", '//section[@class="charge-nav ng-scope"]/div/div[2]/ul/li[6]/a')  # 点击套餐替换
    shoukuan_qushangpin = ("xpath", '//section[@class="charge-nav ng-scope"]/div/div[2]/ul/li[7]/a')  # 点击取商品
    shoukuan_jifen = ("xpath", '//section[@class="charge-nav ng-scope"]/div/div[2]/ul/li[8]/a')  # 点击积分

    # 收款-扣次卡
    shoukuan_sousuokuang = ("xpath", '//section[@class="charge-nav ng-scope"]/div/div[2]/ul/li[1]/a')  # 点击搜索框
    shoukuan_xiangmu = ("xpath", './/div[@class="promotion-product-item-wrap ng-scope"]/div[2]/div[2]/div[1]/div[1]/div')  # 点击项目
    shoukuan_quxuanzeqitaxiangmu = ("xpath", './/div[@class="promotion-product-item-wrap ng-scope"]/div[2]/div[1]/a')  # 点击去选择其他项目

    # 收款-收款开卡-服务
    shoukuan_fuwu = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/div[1]/div/div/ul/li[1]')  # 点击服务tab
    shoukuan_fuwu_sousuokuang = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/div[1]/div[1]/div[2]/product-nav/div/div/input')  # 点击搜索框
    shoukuan_fuwu_one = ("xpath", './/product-nav[@class="pos-content-nav ng-scope ng-isolate-scope"]/div/div[2]/div[2]/div[1]') # 第一个服务

    # 收款-收款开卡-商品
    shoukuan_shangpin = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/div[1]/div/div/ul/li[1]')  # 点击商品tab
    shoukuan_shangpin_sousuokuang = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/div[1]/div[1]/div[2]/goods-nav-v2/div/div/input')  # 点击搜索框

    # 收款-收款开卡-套餐
    shoukuan_taocan = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/div[1]/div/div/ul/li[1]')  # 点击套餐tab
    shoukuan_taocan_sousuokuang = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/div[1]/div[1]/div[2]/promotion-nav/div/div/div/input')  # 点击搜索框

    # 收款-收款开卡-新增套餐
    shoukuan_taocan_xinzengtaocan = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/div[1]/div[1]/div[2]/promotion-nav/div/div[2]/div/a')  # 点击新增套餐

    # 收款-收款开卡-组合
    shoukuan_zuhe = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/div[1]/div/div/ul/li[1]')  # 点击组合tab
    shoukuan_zuhe_sousuokuang = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/div[1]/div[1]/div[2]/preferential-combination-nav/div/div/div/input')  # 点击搜索框

    # 收款-购储值卡
    shoukuan_gouchuzhika_sousuokuang = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-prepaid/div[1]/div[1]/div[1]/div[1]/input')    # 点击搜索框
    shoukuan_xinzengchuzhika = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-prepaid/div[1]/div[1]/div[2]/div[1]/a')  # 点击新增储值卡

    # 收款-购储值卡-新增储值卡
    shoukuan_gouchuzhika_xinzengchuzhika = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-prepaid/div[1]/div[1]/div[2]/div[1]/a')    # 点击新增储值卡

    # 收款-充储值卡

    # 收款-退卡/退商品

    # 收款-护理替换

    # 收款-取商品

    # 收款-积分


    # 收款-销售单右侧快捷支付方式
    shoukuan_tuikazhanghuyue = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/div[1]/div[3]/div[2]/payment-balance-v2/div/div/div/div/div/div[2]/div/input')
    shoukuan_Cash = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/div[1]/div[3]/div[2]/combination-payment-v2/div[1]/div[1]/div[1]/div[2]/input')
    shoukuan_Bank_Card = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/div[1]/div[3]/div[2]/combination-payment-v2/div[1]/div[2]/div[1]/div[2]/input')
    shoukuan_Weixin = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/div[1]/div[3]/div[2]/combination-payment-v2/div[1]/div[3]/div[1]/div[2]/input')
    shoukuan_Alipay = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/div[1]/div[3]/div[2]/combination-payment-v2/div[1]/div[4]/div[1]/div[2]/input')

    # 收款-销售单右侧快捷支付方式-确定支付
    shoukuan_quedingzhifu = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/div[1]/div[3]/div[3]/span')
    shoukuan_sure_queding = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/confirm-pay/div/div[2]/div[3]/button[1]')
    shoukuan_sure_quxiao = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/confirm-pay/div/div[2]/div[3]/button[2]')
    shoukuan_sure = ("xpath", '//div[@class="alert animated main-alert alert-success zoomOut alert-hidden"]/ul/li') # 支付成功提醒

    # 收款-销售单-支付成功-手工&业绩分配-立即分配
    shoukuan_yejifenpei_lijifenpei = ("xpath", '//div[@id="ngdialog1"]/div[2]/div[3]/button[1]') # 手工&业绩分配
    shoukuan_xiaoshouyeji = ("xpath", '//div[@class="tab-item ng-scope active"]') # 销售业绩tab
    shoukuan_xiaoshouticheng = ("xpath", '//div[@class="tab-item ng-scope active"]')  # 销售提成tab
    shoukuan_xiaohaoyeji = ("xpath", '//div[@class="tab-item ng-scope active"]')  # 消耗业绩tab
    shoukuan_shougong = ("xpath", '//div[@class="tab-item ng-scope active"]')  # 手工/part-tab


    # 收款-销售单-支付成功-手工&业绩分配-暂不分配
    shoukuan_yejifenpei_zanbufenpei = ("xpath", '//div[@id="ngdialog1"]/div[2]/div[3]/button[2]') # 暂不分配



    # 收款-更多支付方式-临时账户
    shoukuan_gengduozhifufagnshi = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/div[1]/div[3]/div[3]/div[1]/a')
    shoukuan_tuikazhanghuyue1 = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/payment-methods-v2/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/input')
    shoukuan_xianxiajifen = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/payment-methods-v2/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div[2]/input')
    shoukuan_xianjinquan = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/payment-methods-v2/div[1]/div/div[2]/div[1]/div[3]/div[1]/div/div[2]/input')

    # 收款-更多支付方式-非收入计消耗
    shoukuan_zidingyiaaaa = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/payment-methods-v2/div[1]/div/div[2]/div[1]/div[4]/div[1]/div/div[2]/input')

    # 收款-更多支付方式
    shoukuan_zidingyi1 = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/payment-methods-v2/div[1]/div/div[2]/div[2]/div/div/div/div[2]/input')
    shoukuan_xianjin = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/payment-methods-v2/div[1]/div/div[2]/div[3]/div[1]/div/div/div[2]/input')
    shoukuan_yinhangka = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/payment-methods-v2/div[1]/div/div[2]/div[3]/div[2]/div/div/div[2]/input')
    shoukuan_weixin = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/payment-methods-v2/div[1]/div/div[2]/div[3]/div[3]/div/div/div[2]/input')
    shoukuan_zhifubao = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/payment-methods-v2/div[1]/div/div[2]/div[3]/div[4]/div/div/div[2]/input')
    shoukuan_EPS = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/payment-methods-v2/div[1]/div/div[2]/div[3]/div[5]/div/div/div[2]/input')
    shoukuan_zhipiao = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/payment-methods-v2/div[1]/div/div[2]/div[3]/div[6]/div/div/div[2]/input')
    shoukuan_Nets = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/payment-methods-v2/div[1]/div/div[2]/div[3]/div[7]/div/div/div[2]/input')

    # 收款-更多支付方式-信用卡、支票等方式
    shoukuan_xinyongka = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/payment-methods-v2/div[1]/div/div[2]/div[4]/div[1]/div[1]/div/div[2]/input')
    shoukuan_AE = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/payment-methods-v2/div[1]/div/div[2]/div[4]/div[1]/div[2]/div/div[2]/input')
    shoukuan_VISA = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/payment-methods-v2/div[1]/div/div[2]/div[4]/div[2]/div[1]/div/div[2]/input')
    shoukuan_UNIONPAY = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/payment-methods-v2/div[1]/div/div[2]/div[4]/div[2]/div[2]/div/div[2]/input')
    shoukuan_MASTER = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/payment-methods-v2/div[1]/div/div[2]/div[4]/div[3]/div[1]/div/div[2]/input')
    shoukuan_JCB = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/payment-methods-v2/div[1]/div/div[2]/div[4]/div[3]/div[2]/div/div[2]/input')
    shoukuan_DINERS = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/payment-methods-v2/div[1]/div/div[2]/div[4]/div[4]/div[1]/div/div[2]/input')

    # 收款-更多支付方式-分期付款
    shoukuan_zhongguoyinhang = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/payment-methods-v2/div[1]/div/div[2]/div[6]/div[1]/div[1]/div[1]/div[2]/input')

    # 收款-更多支付方式-确定支付
    shoukuan_quedingzhifu1 = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/payment-methods-v2/div[1]/div/div[3]/button[1]')

    # 收款-更多支付方式-取消
    shoukuan_quxiao = ("xpath", '//article[@class="charge-v2 flex"]/section[3]/charge-pos/payment-methods-v2/div[1]/div/div[3]/button[2]')


    # def click_shoukuan(self):
    #     '''点击收款菜单'''
    #     self.click(self.Shoukuan_loc)
    #     time.sleep(0.5)
    #
    # def click_sousuokuang(self):
    #     '''点击搜索框'''
    #     self.click(self.search_loc)
    #     time.sleep(0.5)
    #
    # def click_onemember(self):
    #     '''选择下拉框第一个会员'''
    #     self.click(self.onemember)
    #     time.sleep(0.5)
    #
    # # '''
    # # 收款-新增会员
    # # '''
    # # def click_huiyuanguanli(self):
    # #     '''点击会员管理菜单'''
    # #     self.click(self.huiyuan_guanli)
    # #
    # # def click_huiyuan(self):
    # #     '''点击新增会员'''
    # #     self.click(self.huiyuan_xinzeng)
    # #     time.sleep(0.5)
    # #
    # # def input_member_jiancheng(self, name):
    # #     '''点击输入会员简称'''
    # #     self.sendKeys(self.member_jiancheng, name)
    # #
    # # def input_member_leixing(self, leixing):
    # #     '''点击输入会员类型'''
    # #     self.sendKeys(self.member_leixing, leixing)
    # #
    # # def input_member_yingwenming(self, yingwenming):
    # #     '''点击输入会员英文名'''
    # #     self.sendKeys(self.huiyuan_yingwenming, yingwenming)
    # #
    # # def input_member_mingcheng(self, mingcheng):
    # #     '''点击输入会员名称'''
    # #     self.sendKeys(self.huiyuan_mingcheng, mingcheng)
    # #
    # # def input_member_shoujihao(self, phone):
    # #     '''点击输入会员手机号'''
    # #     self.sendKeys(self.huiyuan_shoujihao, phone)
    # #
    # # # def input_member_shenfenzheng(self, shenfenzheng):
    # # #     '''点击输入会员身份证号'''
    # # #     self.sendKeys(self.huiyuan_shenfenzheng, shenfenzheng)
    # #
    # # def click_cancel(self):
    # #     '''点击取消按钮'''
    # #     self.click(self.huiyuan_btn_normal_loc)
    # #
    # # def click_save(self):
    # #     '''点击保存按钮'''
    # #     self.click(self.huiyuan_btn_loc)
    # #
    # '''
    # 收款-选择服务
    # '''
    # def click_chooseservice(self):
    #     '''点击选择第一个服务'''
    #     self.click(self.shoukuan_fuwu_one)
    #
    # '''
    # 收款-销售单右侧
    # '''
    # def click_cash(self):
    #     '''现金支付'''
    #     self.sendKeys(self.shoukuan_Cash)
    #
    # def input_cash(self, cash):
    #     '''现金支付'''
    #     self.sendKeys(self.shoukuan_Cash, cash)
    #
    # def click_queding(self):
    #     '''确定支付'''
    #     self.click(self.shoukuan_quedingzhifu)
    #
    # def click_surequeding(self):
    #     '''二次确定'''
    #     self.click(self.shoukuan_sure_queding)







