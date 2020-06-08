from Base.Base import Base
import Page

# 继承Base类
class Dev_Title(Base):

    def __int__(self,driver):

        # 初始化父类
        Base.__init__(self,driver)

    def click_add(self):

        # 添加文章
        self.click_element(Page.dev_add_title)

    def change_login(self):
        # 选择登录方式：密码登录
        self.click_element(Page.dev_login_pwd)

    def login(self,phone,pwd):
        # 登录
        # 输入手机号码
        self.input_element(Page.dev_input_phone,phone)
        # 输入密码
        self.input_element(Page.dev_input_pwd,pwd)
        # 点击登录
        self.click_element(Page.dev_login_btn)