
"""
    appium方法二次封装
"""
from selenium.webdriver.support.wait import WebDriverWait


class Base():

    def __init__(self,driver):
        # 初始化的driver传进来赋值给自己的变量self.driver
        self.driver = driver

    def find_ele(self,loc,timeout=10,poll=0.5):
        # alt+enter 或者ctrl+alt+空格
        # return self.driver.find_element(*loc)
        return WebDriverWait(self.driver,timeout,poll)\
            .until(lambda x: x.find_element(*loc))

    def find_eles(self,loc,timeout=10,poll=0.5):
        # alt+enter 或者ctrl+alt+空格
        # return self.driver.find_element(*loc)
        return WebDriverWait(self.driver,timeout,poll)\
            .until(lambda x: x.find_elements(*loc))

    def is_disp(self,loc):
        # 判断元素是否存在
        try:
            self.find_ele(loc)
            return True
        except Exception as e:
            return False

    def click_element(self,loc):
        # 点击元素函数
        self.find_ele(loc).click()

    def input_element(self,loc,data):
        ele = self.find_ele(loc)
        ele.clear()
        ele.send_keys(data)