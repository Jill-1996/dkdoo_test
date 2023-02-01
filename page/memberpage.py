# coding:utf-8

from common.BasePage import BasePage
import time


class MemberPage():
    # 会员-会员管理菜单
    huiyuan_guanli = ("xpath", ".//ul[@class='nav ng-scope']/li[1]")
    # 基本信息
    # huiyuan_loc = ("xpath", '//*[text()="新增会员"]')  # 新增会员
    huiyuan_xinzeng = ("xpath", '//*[text()="新增会员"]')  # 新增会员
    # huiyuan_loc = ("xpath", '//span[@class="u-name white-hidden f-middle f-blue"]')  # 新增会员
    huiyuan_jianchen = ("xpath", '//div[@class="m-memberadd new-member"]/div[2]/input[1]')  # 会员简称输入框
    huiyuan_leixing = ("xpath", '//div[@class="m-memberadd new-member"]/div[2]/input[2]')  # 会员类型输入框
    huiyuan_yingwenming = ("xpath", '//div[@class="m-memberadd new-member"]/div[3]/input')  # 会员英文名输入框
    huiyuan_jibie = ("xpath", '//div[@class="m-memberadd new-member"]/div[3]/dkd-select/div/div/ul/li[2/a]')  # 会员级别选择框
    huiyuan_mingcheng = ("xpath", '//div[@class="m-memberadd new-member"]/div[4]/input')  # 会员名称输入框
    huiyuan_zhucemendian = ("xpath", '//div[@class="m-memberadd new-member"]/div[4]/div[3]')  # 注册门店显示
    huiyuan_kahao = ("xpath", '//div[@class="m-memberadd new-member"]/div[5]/div[2]/input')  # 卡号输入框
    huiyuan_zidongluru = ("xpath", '//div[@class="m-memberadd new-member"]/div[5]/div[2]/div')  # 自动录入功能
    huiyuan_genjinyuangong = ("xpath", '//div[@class="m-memberadd new-member"]/div[5]/employee-select/div/span/dkd-multi-select/div/div[1]/div')  # 跟进员工输入框
    huiyuan_gjquanxuan = ("xpath", '//div[@class="m-memberadd new-member"]/div[5]/employee-select/div/span/dkd-multi-select/div/div[2]/div/button[1]')  # 全选按钮
    huiyuan_gjqingkong = ("xpath", '//div[@class="m-memberadd new-member"]/div[5]/employee-select/div/span/dkd-multi-select/div/div[2]/div/button[2]')  # 清空按钮
    huiyuan_one = ("xpath", '//div[@class="m-memberadd new-member"]/div[5]/employee-select/div/span/dkd-multi-select/div/div[2]/loading//div/div/div/div/div/div')  # 选择下拉框第一个选项
    huiyuan_shoujihao = ("xpath", '//div[@class="m-memberadd new-member"]/div[6]/div[2]/input')  # 手机号码输入框
    huiyuan_zhuceshijian1 = ("xpath", '//div[@class="m-memberadd new-member"]/div[6]/div[4]/a/input')  # 注册时间选择框
    huiyuan_zhuceshijian2 = ("xpath", '//div[@class="m-memberadd new-member"]/div[6]/div[4]/span/div/table/tbody/tr[1]/td[1]')  # 注册时间选择框-选择该月第一行第一个数字
    huiyuan_xingbie = ("xpath", '//div[@class="m-memberadd new-member"]/div[7]/div[2]/label[1]/input')  # 性别选择-选择女
    huiyuan_kouka1 = ("xpath", '//div[@class="m-memberadd new-member"]/div[7]/div[4]/member-select/input')  # 扣卡会员选择框
    huiyuan_kouka2 = ("xpath", '//div[@class="m-memberadd new-member"]/div[7]/div[4]/member-select/ul/li[1]/span[1]')  # 扣卡会员选择第一个选项
    huiyuan_birthday_year_loc = ("xpath", '//div[@class="m-memberadd new-member"]/div[8]/div[2]/div/select[1]/option[3]')  # 生日选择框-年份
    huiyuan_birthday_month_loc = ("xpath", '//div[@class="m-memberadd new-member"]/div[8]/div[2]/div/select[2]/option[3]')  # 生日选择框-月份
    huiyuan_birthday_loc = ("xpath", '//div[@class="m-memberadd new-member"]/div[8]/div[2]/div/select[3]/option[3]')  # 生日选择框-日
    huiyuan_jieshaoren1 = ("xpath", '//div[@class="m-memberadd new-member"]/div[8]/div[4]/member-select/input')  # 介绍人1选择框
    huiyuan_shenfenzheng = ("xpath", '//div[@class="m-memberadd new-member"]/div[9]/input')  # 身份证输入框
    huiyuan_jieshaoren2 = ("xpath", '//div[@class="m-memberadd new-member"]/div[9]/div[3]/member-select/input')  # 介绍人2选择框
    huiyuan_jinjilianxiren = ("xpath", '//div[@class="m-memberadd new-member"]/div[10]/input')  # 紧急联系人输入框
    huiyuan_jieshaoren3 = ("xpath", '//div[@class="m-memberadd new-member"]/div[10]/div[3]/member-select/input')  # 介绍人3选择框
    huiyuan_age_group = ("xpath", '//div[@class="m-memberadd new-member"]/div[11]/input[1]')  # 年龄组别输入框
    huiyuan_lianxirendianhua = ("xpath", '//div[@class="m-memberadd new-member"]/div[11]/input[2]')  # 联系人电话输入框
    huiyuan_baoxianziliao = ("xpath", '//div[@class="m-memberadd new-member"]/div[12]/textarea')  # 保险资料输入框
    huiyuan_huiyuangongsi = ("xpath", '//div[@class="m-memberadd new-member"]/div[13]/textarea')  # 会员公司输入框
    huiyuan_xuanchuanziliao = ("xpath", '//div[@class="m-memberadd new-member"]/div[14]/input')  # 宣传资料输入框
    huiyuan_qitadianhuaziliao = ("xpath", '//div[@class="m-memberadd new-member"]/div[15]/input')  # 其他电话资料输入框
    huiyuan_laiyaun1 = ("xpath", '//div[@class="m-memberadd new-member"]/div[16]/div[2]/div/dkd-multi-select/div/div/div[1]')  # 会员来源选择框
    huiyuan_laiyuan2 = ("xpath", '//div[@class="m-memberadd new-member"]/div[16]/div[2]/div/dkd-multi-select/div/div/span')  # 会员来源点击下拉框
    huiyuan_lyquanxuan = ("xpath", '//div[@class="m-memberadd new-member"]/div[16]/div[2]/div/dkd-multi-select/div/div[2]/div/button[1]')  # 全选按钮
    huiyuan_lyqingkogn = ("xpath", '//div[@class="m-memberadd new-member"]/div[16]/div[2]/div/dkd-multi-select/div/div[2]/div/button[2]')  # 清空按钮
    huiyuan_laiyuanone = ("xpath", '//div[@class="m-memberadd new-member"]/div[16]/div[2]/div/dkd-multi-select/div/div[2]/loading/div/div/div[1]/div/div')  # 会员来源选择第一个选项
    huiyuan_laiyuan3 = ("xpath", '//div[@class="m-memberadd new-member"]/div[16]/div[2]/div[2]/input')  # 会员来源输入框
    huiyuan_beizhu = ("xpath", '//div[@class="m-memberadd new-member"]/div[17]/textarea')  # 备注输入框
    huiyuan_zhuagntai = ("xpath", '//div[@class="m-memberadd new-member"]/div[18]/span')  # 状态选择
    huiyuan_zhidingfuwu = ("xpath", '//div[@class="m-memberadd new-member"]/div[18]/employee-select')  # 指定服务员工选择框
    huiyuan_zdquanxuan = ("xpath", '//div[@class="m-memberadd new-member"]/div[18]/employee-select/div/div/div/span/div/div/div/button[1]')  # 全选按钮
    huiyuan_zdqingkong = ("xpath", '//div[@class="m-memberadd new-member"]/div[18]/employee-select/div/div/div/span/div/div/div/button[2]')  # 清空按钮
    huiyuan_zdfuwu = ("xpath", '//div[@class="m-memberadd new-member"]/div[18]/employee-select/div/div/div/span/div/div[2]/div[1]/div/label/span')  # 指定服务员工选择第一个选项
    huiyuan_yuyueduanxin = ("xpath", '//div[@class="m-memberadd new-member"]/div[19]/select')  # 预约短信中英文选择框
    huiyuan_Appointment_SMS1 = ("xpath", '//div[@class="m-memberadd new-member"]/div[19]/select/option[1]')  # 预约短信中英文选择第一个选项（空白项）
    huiyuan_Appointment_SMS2 = ("xpath", '//div[@class="m-memberadd new-member"]/div[19]/select/option[2]')  # 预约短信中英文选择第二个选项
    huiyuan_Appointment_SMS3 = ("xpath", '//div[@class="m-memberadd new-member"]/div[19]/select/option[3]')  # 预约短信中英文选择第三个选项

    # 标签信息
    huiyuan_zhankaibiaoqian = ("xpath", '//div[@class="m-memberadd new-member"]/div[20]/span')  # 展开标签信息
    huiyuan_mingzu = ("xpath", '//div[@class="m-memberadd new-member"]/div[21]/div[1]/select')  # 民族选择框
    huiyuan_mingzuone = ("xpath", '//div[@class="m-memberadd new-member"]/div[21]/div[1]/select/option[1]')  # 民族选择框第一个选项-空白
    huiyuan_mingzutwo = ("xpath", '//div[@class="m-memberadd new-member"]/div[21]/div[1]/select/option[2]')  # 民族选择框第二个选项
    huiyuan_yinshixiguan = ("xpath", '//div[@class="m-memberadd new-member"]/div[21]/div[1]/input')  # 饮食习惯输入框
    huiyuan_aihao = ("xpath", '//div[@class="m-memberadd new-member"]/div[21]/div[2]/input[1]')  # 爱好输入框
    huiyuan_gerenjinji = ("xpath", '//div[@class="m-memberadd new-member"]/div[21]/div[3]/input[2]')  # 个人禁忌输入框
    huiyuan_xingge = ("xpath", '//div[@class="m-memberadd new-member"]/div[21]/div[3]/input[1]')  # 性格输入框
    huiyuan_jiatingqingkuang = ("xpath", '//div[@class="m-memberadd new-member"]/div[21]/div[3]/input[2]')  # 家庭情况输入框
    huiyuan_hunfouyihun = ("xpath", '//div[@class="m-memberadd new-member"]/div[21]/div[4]/div[1]/label[1]')  # 婚否选择-已婚
    huiyuan_hunfouweihun = ("xpath", '//div[@class="m-memberadd new-member"]/div[21]/div[4]/div[1]/label[2]')  # 婚否选择-未婚
    huiyuan_suoshuhangye = ("xpath", '//div[@class="m-memberadd new-member"]/div[21]/div[4]/input')  # 所属行业输入框
    huiyuan_zhiye = ("xpath", '//div[@class="m-memberadd new-member"]/div[21]/div[5]/input[1]')  # 职业输入框
    huiyuan_jiaoyuchengdu = ("xpath", '//div[@class="m-memberadd new-member"]/div[21]/div[5]/input[2]')  # 教育程度输入框
    huiyuan_shengao = ("xpath", '//div[@class="m-memberadd new-member"]/div[21]/div[6]/input[1]')  # 身高输入框
    huiyuan_meiyueshouru = ("xpath", '//div[@class="m-memberadd new-member"]/div[21]/div[6]/input[2]')  # 每月收入输入框
    huiyuan_tizhong = ("xpath", '//div[@class="m-memberadd new-member"]/div[21]/div[7]/input[1]')  # 体重输入框
    huiyuan_xiaihuati = ("xpath", '//div[@class="m-memberadd new-member"]/div[21]/div[7]/input[2]')  # 喜爱话题输入框
    huiyuan_tizhi = ("xpath", '//div[@class="m-memberadd new-member"]/div[21]/div[8]/input')  # 体质输入框

    # 护理信息
    huiyuan_zhankaihulixinxi = ("xpath", '//div[@class="m-memberadd new-member"]/div[22]/span')  # 展开护理信息
    huiyuan_guominshi = ("xpath", '//div[@class="m-memberadd new-member"]/div[23]/div[1]/input')  # 过敏史输入框
    huiyuan_hulizhuangtai1 = ("xpath", '//div[@class="m-memberadd new-member"]/div[23]/div[1]/div/label[1]')  # 护理状态选择-从未
    huiyuan_hulizhuangtai2 = ("xpath", '//div[@class="m-memberadd new-member"]/div[23]/div[1]/div/label[2]')  # 护理状态选择-偶然
    huiyuan_hulizhuangtai3 = ("xpath", '//div[@class="m-memberadd new-member"]/div[23]/div[1]/div/label[3]')  # 护理状态选择-经常
    huiyuan_binglishi = ("xpath", '//div[@class="m-memberadd new-member"]/div[23]/div[2]/input')  # 病例史输入框
    huiyuan_zuihouhuliriqi1 = ("xpath", '//div[@class="m-memberadd new-member"]/div[23]/div[2]/div[3]/a/span/input')  # 最后护理日期选择框
    huiyuan_zuihouhuliriqi2 = ("xpath", '//div[@class="m-memberadd new-member"]/div[23]/div[2]/div[3]/span/div/table/tbody/tr[1]/td[1]')  # 最后护理日期选择框-选择该月第一行第一个数字
    huiyuan_manxinbing = ("xpath", '//div[@class="m-memberadd new-member"]/div[23]/div[3/input[1]]')  # 慢性病输入框
    huiyuan_lijiashijian = ("xpath", '//div[@class="m-memberadd new-member"]/div[23]/div[3/input[2]]')  # 例假时间输入框
    huiyuan_pifuxingzhi = ("xpath", '//div[@class="m-memberadd new-member"]/div[23]/div[4]/div[2]/div[1]/div[2]/label[1]/input')  # 皮肤性质选择-选择第一行的第一个选项

    # 其他信息
    huiyuan_zhankaiqitaxinxi = ("xpath", '//div[@class="m-memberadd new-member"]/div[24]/span')  # 展开其他信息
    huiyuan_qq = ("xpath", '//div[@class="m-memberadd new-member"]/div[25]/div[1]/input[1]')  # QQ输入框
    huiyuan_dianyou = ("xpath", '//div[@class="m-memberadd new-member"]/div[25]/div[1]/input[2]')  # 电邮输入框
    huiyuan_weixin = ("xpath", '//div[@class="m-memberadd new-member"]/div[25]/div[2]/input[1]')  # 微信输入框
    huiyuan_chuanzhenhaoma = ("xpath", '//div[@class="m-memberadd new-member"]/div[25]/div[2]/input[2]')  # 传真号码输入框
    huiyuan_jiatingdizhi1 = ("xpath", '//div[@class="m-memberadd new-member"]/div[25]/div[3]/country-select/select')  # 家庭地址选择框
    huiyuan_jiatingdizhi2 = ("xpath", '//div[@class="m-memberadd new-member"]/div[25]/div[3]/country-select/select/option[2]')  # 家庭地址选择框-选择第二个选项
    huiyuan_jtxiangxidizhi = ("xpath", '//div[@class="m-memberadd new-member"]/div[25]/div[4]/textarea')  # 详细地址输入框
    huiyuan_jtdaodianjuli = ("xpath", '//div[@class="m-memberadd new-member"]/div[25]/div[5]/input')  # 到店距离输入框
    huiyuan_gognsidizhi1 = ("xpath", '//div[@class="m-memberadd new-member"]/div[25]/div[6]/country-select/select')  # 公司地址选择框
    huiyuan_gognsidizhi2 = ("xpath", '//div[@class="m-memberadd new-member"]/div[25]/div[6]/country-select/select/option[2]')  # 公司地址选择框-选择第二个选项
    huiyuan_gsxiangxidizhi = ("xpath", '//div[@class="m-memberadd new-member"]/div[25]/div[7]/textarea')  # 详细地址输入框
    huiyuan_gsdaodianjuli = ("xpath", '//div[@class="m-memberadd new-member"]/div[25]/div[8]/input')  # 到店距离输入框
    huiyuan_changyogndizhi1 = ("xpath", '//div[@class="m-memberadd new-member"]/div[25]/div[9]/country-select/select')  # 常用地址选择框
    huiyuan_changyogndizhi2 = ("xpath", '//div[@class="m-memberadd new-member"]/div[25]/div[9]/country-select/select/option[2]')  # 常用地址选择框-选择第二个选项
    huiyuan_cyxiagnxidizhi = ("xpath", '//div[@class="m-memberadd new-member"]/div[25]/div[10]/textarea')  # 详细地址输入框
    huiyuan_cydaodianjuli = ("xpath", '//div[@class="m-memberadd new-member"]/div[25]/div[11]/div')  # 到店距离输入框
    huiyuan_qtdizhi1 = ("xpath", '//div[@class="m-memberadd new-member"]/div[25]/div[12]/country-select/select')  # 其他地址选择框
    huiyuan_qtdizhi2 = ("xpath", '//div[@class="m-memberadd new-member"]/div[25]/div[12]/country-select/select/option[2]')  # 其他地址选择框-选择第二个选项
    huiyuan_qtxiagnxidizhi = ("xpath", '//div[@class="m-memberadd new-member"]/div[25]/div[13]/textarea')  # 详细地址输入框
    huiyuan_qtdaodianjuli = ("xpath", '//div[@class="m-memberadd new-member"]/div[25]/div[14]/input')  # 到店距离输入框

    huiyuan_btn_normal_loc = ("xpath", '//div[@class="pull-left main"]/ng-outlet/member-maintenance/div/div/member-list/member-added/div/header/div[1]')  # 取消按钮
    huiyuan_btn_loc = ("xpath", '//div[@class="pull-left main"]/ng-outlet/member-maintenance/div/div/member-list/member-added/div/header/div[2]') # 保存按钮

    # def click_inmember(self):
    #     '''进入会员管理页面'''
    #     self.click(self.huiyuan_guanli)
    #
    # def click_newmember(self):
    #     '''点击新增会员按钮'''
    #     self.click(self.huiyuan_xinzeng)
    #
    # def input_membername(self, membername):
    #     '''输入会员简称'''
    #     self.sendKeys(self.huiyuan_jianchen, membername)
    #
    # def input_phonenumber(self, phonenumber):
    #     '''输入手机号码'''
    #     self.sendKeys(self.huiyuan_shoujihao, phonenumber)
    #
    # def click_baocun(self):
    #     '''点击保存按钮'''
    #     self.click(self.huiyuan_btn_loc)
