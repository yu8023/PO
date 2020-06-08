
from selenium.webdriver.common.by import By
from Base.Base import Base
import Page


class Search_Page(Base):

    def __init__(self,driver):

        # 父类初始化方法
        Base.__init__(self,driver)
        # # 1、用到的元素和定位方法
        # # 搜索按钮
        # self.search_button = (By.ID, "com.android.settings:id/search")
        # # 搜索输入框
        # self.search_input = (By.ID, "android:id/search_src_text")
        # # 搜索框返回按钮
        # self.search_return_button = (By.CLASS_NAME, "android.widget.ImageButton")

        # # 初始化的driver传进来赋值给自己的变量self.driver
        # self.driver = driver
        # # 2、实例化Base类
        # self.base_obj = Base(self.driver)

    def click_search(self):
        # 点击搜索按钮
        self.click_element(Page.search_button)

    def input_search(self,input_text):
        # 输入搜索内容
        self.input_element(Page.search_input,input_text)

    def click_return(self):
        # 点击返回按钮
        self.click_element(Page.search_return_button)

    def search_text(self,data):
        # 3、对元素的操作
        # 点击搜索按钮
        self.click_element(Page.search_button)
        # 输入内容
        self.input_element(Page.search_input,data)
        # 点击返回按钮
        self.click_element(Page.search_return_button)




