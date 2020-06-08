
from selenium.webdriver.common.by import By
from Base.Base import Base
import Page,allure

class Add_Person(Base):

    def __init__(self,driver):
        # 初始化父类
        Base.__init__(self, driver)

    # 3、对元素的操作
    def add_p_btn(self):
        self.click_element(Page.add_p)

    def click_left_btn(self):
        self.click_element(Page.left_button)

    def input_user_info(self,name,phone):
        # 测试描述
        allure.attach("输入用户名","描述")
        # 输入用户名
        self.input_element(Page.name_input,name)
        allure.attach("输入手机号操作","描述")
        # 输入电话号码
        self.input_element(Page.phone_input,phone)
        allure.attach("点击添加页面保存√","描述")
        # 点击返回保存按钮
        self.click_element(Page.save_button)
        # 判断是否在用户详情页
        if self.is_disp(Page.user_edit_btn):
            allure.attach("点击手机返回键","描述")
            self.driver.keyevent(4)

    def get_user_list(self):
        # 获取联系人列表
        user_info =(By.ID, "com.android.contacts:id/cliv_name_textview")
        person_text_list = self.find_eles(user_info)
        # 普通方法
        # person_list = []
        # for i in person_text_list:
        #     person_list.append(i.text)

        # 列表解析
        person_list = [i.text for i in person_text_list]
        print(person_list)       # <class 'list'>    ['abc', '丁丁', 'dingding']
        return  person_list





