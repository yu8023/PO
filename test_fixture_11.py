import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import os

def info():
    return [("好文章", "http://www.baidu.com"),("java", "http://www.google.com")]

class Test_SMS_Simple:
    def setup_class(self):
        # 用户登录信息
        # self.user_info = {"user":"benbenxiong567@163.com","pwd":"139432500"}
        # server 启动参数
        desired_caps = {}
        # 系统
        desired_caps['platformName'] = 'Android'
        # 版本
        desired_caps['platformVersion'] = '6.0'
        # 设备号
        os.system("adb devices")
        desired_caps['deviceName'] = '192.168.140.101:5555'
        # app的信息
        desired_caps['appPackage'] = 'io.manong.developerdaily'
        desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.MainActivity'
        # 中文输入允许
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        # 声明我们的driver对象
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def teardown_class(self):
        # 关闭驱动对象，同时关闭所有关联的app
        self.driver.quit()

    def wait_element(self, type, data):
        if type == "id":
            return WebDriverWait(self.driver, 10, 2)\
                .until(lambda x: x.find_element_by_id(data))
        if type == "id_more":
            return WebDriverWait(self.driver, 10, 2)\
                .until(lambda x: x.find_elements_by_id(data))

        if type == "xpath":
            return WebDriverWait(self.driver, 10, 2)\
                .until(lambda x: x.find_element_by_xpath(data))

    # 登录操作
    @pytest.fixture(params=[("benbenxiong567@163.com","139432500")])        # 标记为fixture：工厂函数 优先执行
    def if_login(self, request):
        # 用户名密码
        user, pwd = request.param
        print("user....:",user)
        print("pwd....:",pwd)
        # 进入我的页面
        self.wait_element("xpath", "//*[contains(@text,'我')]").click()
        # 查看是否是登录状态，定位申请独家账号
        text_data = self.wait_element("xpath", "//*[contains(@text,'申请')]")
        print(text_data.text)
        if "我的独家" in text_data.text:
            # 未登录状态
            # 点击登录按钮
            self.wait_element("id", "io.manong.developerdaily:id/login_btn").click()
            # 选择邮箱登录
            self.wait_element("xpath", "//*[contains(@text,'邮箱登录')]").click()
            # 输入用户名
            self.wait_element("id", "io.manong.developerdaily:id/edt_email").send_keys(user)
            # 输入密码
            self.wait_element("id", "io.manong.developerdaily:id/edt_password").send_keys(pwd)
            # 点击登录按钮
            self.wait_element("id","io.manong.developerdaily:id/btn_login").click()

    # 函数引用
    @pytest.mark.usefixtures("if_login")            #调用fixture标记的工厂函数，判断是否登录
    # 函数数据参数化
    @pytest.mark.parametrize("title, url", info())      # 传入需要的参数值
    def test_adduser_sendsms(self, title, url):
        # 定位添加按钮
        self.wait_element("id", "io.manong.developerdaily:id/tab_bar_plus").click()
        # 定位文章标题
        self.wait_element("xpath", "//*[contains(@text,'文章标题')]").send_keys(title)
        # 定位原始链接
        self.wait_element("xpath", "//*[contains(@text,'原始链接')]").send_keys(url)
        # 点击右上角提交按钮
        self.wait_element("id","io.manong.developerdaily:id/action_done").click()
        assert True

if __name__ == "__main__":
    pytest.main("-s test_fixture_011.py")