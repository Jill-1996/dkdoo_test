# coding:utf-8

from common.BasePage import BasePage

# loginurl = "http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html"
loginurl = "http://192.168.31.228:8000/?26#/login"


# 继承于BasePage
class LoginPage(BasePage):
    '''登录页面'''
    phoneNo_loc = ("id", "phoneNo")  # 输入账号
    password_loc = ("id", "password")  # 输入密码
    denglu_loc = ("xpath", ".//div[@class='col-lg-12 loginContainer']/form/div[5]/a/button")    # 点登录
    jizhu_loc = ("id", "rememberme") # 点击记住用户名
    wangjimima_loc = ("class", "forgot-password u-register f-cursor")  # 点击忘记密码
    lianxiwomen_loc = ("xpath", "//*[text()='联系我们']")  # 点击联系我们
    qiehuan_loc = ("xpath", ".//div[@class='inline-block accout-switch ng-binding ng-scope']/a")  # 点击非中国内地用户，点击这里
    tuichu_loc = ("xpath", ".//div[@class='m-news pull-right dropdown']/span[10]/user-profile/div/ul/li[5]/span")
    tuichuqueren_loc = ("xpath", ".//div[@id='ngdialog1']/div[2]/div[3]/button[1]")
    tuichuquxiao_loc = ("xpath", ".//div[@id='ngdialog1']/div[2]/div[3]/button[2]")
    zhanghao_loc = ("xpath", ".//div[@class='m-news pull-right dropdown']/span[8]/user-profile/span") # 定位账号
    denglushibai1_loc = ("xpath", ".//div[@class='alert animated main-alert alert-warning zoomOut alert-hidden']/h5/strong")
    denglushibai2_loc = ("xpath", ".//div[@class='alert animated main-alert alert-warning zoomOut alert-hidden']/ul/li")
    dengluchenggong_loc = ("xpath", ".//div[@class='alert animated main-alert alert-success zoomOut alert-hidden']/ul/li")


    def open_login_page(self):
        self.driver.get(loginurl)

    def logout(self):
        '''登出'''
        # driver = webdriver.Firefox()
        self.driver.delete_all_cookies() # 删除所有的cookies
        self.driver.refresh()

    def input_phoneNo(self,username):
        '''输入账号'''
        self.sendKeys(self.phoneNo_loc, username)

    def input_password(self, psw):
        '''输入密码'''
        self.sendKeys(self.password_loc, psw)

    def click_login_button(self):
        '''点击登录按钮'''
        self.click(self.denglu_loc)

    def click_jizhu_button(self):
        '''点击记住密码按钮'''
        self.click(self.jizhu_loc)

    def click_wangjimima_button(self):
        '''点击忘记密码按钮'''
        self.click(self.wangjimima_loc)

    def click_lianxiwomen_button(self):
        '''点击联系我们按钮'''
        self.click(self.lianxiwomen_loc)

    def click_qiehuan_button(self):
        '''点击切换按钮'''
        self.click(self.qiehuan_loc)

    # def click_tuichu_button(self):
    #     '''点击右上角账号，展开'''
    #     self.click(self.tuichu_loc)
    #
    # def moveToElement_tuichu(self):
    #     '''鼠标悬停右上角账号，展开'''
    #     self.moveToElement(self.tuichu_loc)

    def click_queren_button(self):
        '''确定退出系统'''
        self.click(self.tuichuqueren_loc)

    def click_quxiao_button(self):
        '''取消退出系统'''
        self.click(self.tuichuquxiao_loc)

    def login(self, username="15012345678", psw="dkd123456"):
        '''登录流程:'''
        self.open_login_page()
        self.input_phoneNo(username)
        self.input_password(psw)
        self.click_login_button()

    def get_login_tishi1(self):
        '''获取登陆失败的结果1'''
        try:
            t = self.findElement(self.denglushibai1_loc).text
            return t
        except:
            print("登录异常1！！！")

    def get_login_tishi2(self):
        '''获取登陆失败的结果2'''
        try:
            t = self.findElement(self.denglushibai2_loc).text
            return t
        except:
            print("登录异常2！！！")

    def get_login_result(self):
        '''获取登录的结果-账号是否与预期一致'''
        try:
            t = self.findElement(self.zhanghao_loc).text
            return t
        except:
            print("登录失败！！！，返回空字符")
            return ""

    def get_login_tishi3(self):
        '''获取登录的结果-成功提示'''
        try:
            t = self.findElement(self.dengluchenggong_loc).text
            return t
        except:
            print("登录异常3！！！")
            return ""

    def is_alert(self):
        '''判断是否有弹窗，有的话点确定，没有的话就pass
        有缺陷：如果页面卡，出现alert慢就判断不到了
        '''
        try:
            alert = self.driver.switch_to_alert()  # 这一步不会报错
            print(alert.text)     # 这一步，没有获取到alert文本就报错了
            alert.accept()  # 点确定按钮
        except:
            pass

    def is_alert_exsits_base(self):
        try:
            alert = self.is_alert_exsit()
            alert.accept()
        except:
            pass
