from appium import webdriver
import os

# 函数定义：函数名init_driver
def init_driver():
    # server 启动参数
    desired_caps = {}
    # 系统
    desired_caps['platformName'] = 'Android'
    # 版本
    desired_caps['platformVersion'] = '6.0'
    # 设备号
    os.system("adb devices")
    desired_caps['deviceName'] = '192.168.140.101:5555'

    os.system("adb shell dumpsys window windows | findstr mFocusedApp")
    # app的信息
    # desired_caps['appPackage'] = 'com.android.settings'         # 设置
    # desired_caps['appActivity'] = '.Settings'
    desired_caps['appPackage'] = 'com.android.contacts'       # 联系人
    desired_caps['appActivity'] = '.activities.PeopleActivity'
    # 中文输入允许
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 声明我们的driver对象
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    # 使用return 语句将函数的运行结果返回给函数的调用者
    return driver

    # data = WebDriverWait(driver,10,0.5).until(lambda x: x.find_element_by_xpath("//*[contains(@text,'dingding')]/.."))
    # print(data.location)                      # {'x': 0, 'y': 704}
    # print(data.get_attribute("className"))      # android.view.ViewGroup

if __name__ == '__main__':

    driver = init_driver()