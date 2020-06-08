
from selenium.webdriver.common.by import By
from Base.Base import Base
import Page

class Send_Sms:
    def __init__(self,driver):

        # 2、实例化Base类
        self.base_obj = Base(driver)

        # # 1、用到的元素和定位方法
        # # 短信页的+号按钮
        # self.add_button = (By.ID,"com.android.messaging:id/start_new_conversation_button")
        # # 收件人
        # self.rec_person = (By.ID,"com.android.messaging:id/recipient_text_view")
        # # 短信内容
        # self.input_sms = (By.ID,"com.android.messaging:id/compose_message_text")
        # # 发送按钮
        # self.send_button = (By.ID,"com.android.messaging:id/self_send_icon")

    # 3、对元素的操作
    def add_sms_btn(self):
        # 点击+号按钮
        self.base_obj.click_element(Page.add_button)

    def accept_person_input(self,phone):
        # 输入收件人
        self.base_obj.input_element(Page.rec_person,phone)

    def send_sms_input(self,data):
        # 输入发送内容
        self.base_obj.input_element(Page.input_sms,data)
        self.base_obj.click_element(Page.send_button)