# coding:utf-8
import self as self
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    '''基于原生的selenium做二次封装'''
    # def __init__(self, driver, base_url='http://www.cnblogs.com/yoyoketang/p/'):
    # def __init__(self, driver, base_url='http://192.168.31.228:8000/#/login'):
    def __init__(self, driver):
        self.driver = driver
        '''启动浏览器参数化，默认启动Chrome'''
        # self.driver = webdriver.Chrome()
        self.timeout = 30
        self.poll = 0.5

    def open(self, url):
        self.driver.get(self.base_url + url)

    def sendKeys(self, loctor, text):
        ele = self.findElement(loctor)
        ele.send_keys(text)

    def click(self, loctor):
        ele = self.findElement(loctor)
        ele.click()

    def clear(self, loctor):
        ele = self.findElement(loctor)
        ele.clear()

    def findElement(self, loctor):
        '''
        args:
        loctor 传元祖，如（"id","xx"）
        '''
        element = WebDriverWait(self.driver, self.timeout, self.poll).until(lambda x: x.find_element(*loctor))
        return element

    def findElementNew(self, loctor):
        # 找到了返回element，没找到抛异常
        element = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.presence_of_element_located(loctor))
        return element

    def findElements(self, loctor):
        '''
        args:
        loctor 传元祖，如（"id","xx"）
        '''
        elements = WebDriverWait(self.driver, self.timeout, self.poll).until(lambda x: x.find_elements(*loctor))
        return elements

    def findElementsNew(self, loctor):
        # 找到了返回list, 没找到抛异常
        elements = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.presence_of_all_elements_located(loctor))
        return elements

    def moveToElement(self, loctor):
        '''鼠标悬停事件'''
        mos = self.findElement(loctor)
        ActionChains(self.driver).move_to_element(mos).perform()

    def is_text_in_element(self, locator, text):
        '''判断给定的text在这个元素的文本上
        要么返回true,要么返回false,不要让它抛异常了
        '''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.text_to_be_present_in_element(locator, text))
            return result
        except:
            return False

    def is_value_in_element(self, locator, value):
        '''判断给定的value在这个元素的文本上
        要么返回true,要么返回false,不要让它抛异常了
        三种情况为假：0，"", None  python是没有null的
        1.找不到元素返回False
        2.value为空返回False
        3.value不在元素的value值里返回False
        '''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.text_to_be_present_in_element_value(locator, value))
            return result
        except:
            return False

    def is_element_exsits(self, locator):
        '''判断元素是否存在；查找元素的时候，存在返回element，不存在的时候Timeout异常了'''
        try:
            self.findElement(locator)
            return True
        except:
            return False

    def is_alert_exsit(self, timeout=5):
         '''判断alert弹窗是否存在；语文老师教的：直到，，，，才，，，
        如有alert,返回的是alert对象，
        没有就返回False'''
         alert = WebDriverWait(self.driver, timeout, self.poll).until(EC.alert_is_present())
         return alert

    def js_scroll_end(self):
        '''滚动到底部'''
        js_heig = "window.scrollTo(0, document.body.scrollHeight)"
        self.driver.execute_script(js_heig)

    def js_focus(self, loctor):
        '''聚焦元素'''
        targe = self.findElement(loctor)
        self.driver.execute_script("arguments[0].scrollIntoView();", targe)

    def js_scroll_top(self):
        '''回到顶部'''
        js = "window.scrollTo(0, 0)"
        self.driver.execute_script(js)


if __name__ == "__main__":
    # if下面的代码都是测试调试的代码，自测内容
    driver = webdriver.Chrome() # 调用浏览器
    web = BasePage(driver)
    driver.get("http://192.168.31.228:8000/#/login") # 打开url，顺便判断打开的页面对不对
    driver.maximize_window()
    import time
    time.sleep(2)
    loc1 = ("id", "phoneNo") # 定位账号输入框
    loc2 = ("id", "password") # 定位密码输入框
    loc3 = ("xpath", ".//div[@class='col-lg-12 loginContainer']/form/div[5]/a/button") # 定位立即登录按钮
    web.sendKeys(loc1, "15012345678") # 输入账号
    web.sendKeys(loc2, "dkd123456") # 输入密码
    web.click(loc3) # 点登录
    time.sleep(2)
    # 退出系统-悬移鼠标至账号
    mos = driver.find_element_by_class_name("u-username")
    ActionChains(driver).move_to_element(mos).perform()
    time.sleep(2)
    # 点击安全退出
    loc4 = ("xpath", ".//div[@class='m-news pull-right dropdown']/span[10]/user-profile/div/ul/li[5]/span")
    time.sleep(2)
    web.click(loc4)
    # 点击确定退出
    loc5 = ("xpath", ".//div[@id='ngdialog1']/div[2]/div[3]/button[1]")
    web.click(loc5)
    time.sleep(2)
    driver.quit()


    # driver.get("http://www.cnblogs.com/yoyoketang/p/")
    # base.js_scroll_end()  # 滚动到底部
    # plun_loc = ("xpath", "//h3[text()='最新评论']")
    # base.js_focus(plun_loc)
    # loc1 = ("id", "kw")  # 定位百度输入框
    # base.sendKeys(loc1, "发送的内容")  # 关键字
    # loc2 = ("css selector", "#su")   # 定位搜索按钮
    # base.click(loc2)
    # news_loc = ("xpath", ".//*[@id='u1']/a[1]")  # 新闻
    # res = base.is_text_in_element(news_loc, "新闻")
    # print(res)
    # btn_loc = ("id", "su")
    # res1 = base.is_value_in_element(btn_loc, "百度一下")
    # print(res1)
    # driver.quit()

