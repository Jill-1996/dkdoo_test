# coding:utf-8

import time
from selenium import webdriver


driver = webdriver.Chrome()
# def set_win_waitTime(self):
driver.maximize_window() # 最大化页面
driver.implicitly_wait(1) # 等待也没按完全加载完成（页面加载完成的标志是左上角转圈结束）


def login(driver, username="15012345678", pwd="dkd123456"):
    driver.get("http://192.168.31.228:8000/#/login")
    time.sleep(1)
    driver.find_element_by_id("phoneNo").send_keys(username)
    driver.find_element_by_id("password").send_keys(pwd)
    driver.find_element_by_class_name("btn").click()
    time.sleep(1)
    try:
        t = driver.find_element_by_class_name("u-username").text
        if t == username:
            print("登录成功，用户名:" + username)
            return t

    except:
        print("登录失败，返回空字符")
        return ""

    driver.find_element("id", "phoneNo")
    driver.find_element("id", "password")
    driver.find_element("class name", "btn")


def logout():
    driver.quit()


if __name__ == "__main__":
    # from selenium import webdriver
    # driver = webdriver.Chrome()
    login(driver)
    # login("15011111111", "dkd123456")
    logout()
