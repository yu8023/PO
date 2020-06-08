import sys,os
sys.path.append(os.getcwd())

from selenium.webdriver.common.by import By
from Base.Base import Base
from Base.InitDriver import init_driver


class Test_Base():

    def setup(self):
        # 实例化init_driver类  # 函数调用 将运行结果(手机驱动对象)返回给函数的调用者driver
        self.driver = init_driver()

        # 实例化二次封装的Base类，把声明的对象丢给Base
        self.base_obj = Base(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_po001(self):

        # 搜索按钮
        search_button = (By.ID, "com.android.settings:id/search")
        # 搜索输入框
        search_input = (By.ID, "android:id/search_src_text")
        # 搜索框返回按钮
        search_return_button = (By.CLASS_NAME, "android.widget.ImageButton")

        # 点击搜索输入框
        self.base_obj.click_element(search_button)
        # 搜索框内输入123
        self.base_obj.input_element(search_input, 123)
        # 点击搜索框返回按钮
        self.base_obj.click_element(search_return_button)

if __name__ == "__main__":
    Test_Base().test_po001()




