import sys,os,pytest
sys.path.append(os.getcwd())

from Page.Page import Page_Obj
from appium import webdriver
import time

class Test_Dev_Login():

    def setup_class(self):
        # server 启动参数
        desired_caps = {}
        # 系统
        desired_caps['platformName'] = 'Android'
        # 版本
        desired_caps['platformVersion'] = '6.0'
        # 设备号
        os.system("adb devices")
        desired_caps['deviceName'] = '192.168.140.101:5555'
        # 不要在会话前重置应用状态
        desired_caps['noReset'] = 'true'

        os.system("adb shell dumpsys window windows | findstr mFocusedApp")
        # app的信息
        desired_caps['appPackage'] = 'io.manong.developerdaily'
        desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.MainActivity'
        # 中文输入允许
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        # 声明我们的driver对象
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        # 实例化类Dev_Title
        self.dev_obj = Page_Obj(self.driver).Dev_T()
        time.sleep(3)

    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture(scope="class")
    def start_step(self):
        # 点击添加文章
        self.dev_obj.click_add()
        # 选择登录方式
        self.dev_obj.change_login()

    @pytest.mark.usefixtures("start_step")
    @pytest.mark.parametrize("phone,pwd",[("1","3333"),("1@qq",""),("15951995831","1qaz")])
    def test_login(self,phone,pwd):
        # 输入手机号码和密码
        self.dev_obj.login(phone,pwd)
        self.driver.get_screenshot_as_file("./screen/login_%s.png"% phone)


