from Page.dev_title import Dev_Title
from Page.search import Search_Page
from Page.sms import Send_Sms

class Page_Obj():

    def __init__(self,driver):

        # 初始化的driver传进来赋值给自己的变量self.driver
        self.driver = driver

    # 使用return 语句将函数的运行结果返回给函数的调用者

    def Dev_T(self):
        # 开发者头条登录
        return Dev_Title(self.driver)

    def Search_Page(self):
        # 设置-搜索
        return Search_Page(self.driver)

    def SMS(self):
        # 短信
        return Send_Sms(self.driver)
