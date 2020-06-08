import sys,os,pytest
sys.path.append(os.getcwd())

from Base.InitDriver import init_driver
from Page.sms import Send_Sms

class Test_sms:
    def setup_class(self):

        self.driver = init_driver()

        # 实例化二次封装的Send_Sms类，把声明的对象丢给Send_Sms
        self.sms_obj = Send_Sms(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("phone", ["15951995831"])
    # @pytest.fixture(params=["15951995831"])
    def test_add_input_phone(self,phone):
        # 点击添加按钮
        self.sms_obj.add_sms_btn()
        # 输入手机号
        self.sms_obj.accept_person_input(phone)
        # 回车键
        self.driver.keyevent(66)

    @pytest.mark.parametrize("data",["你好","hello","在吗？"])
    def test_po003(self,data):
        self.sms_obj.send_sms_input(data)
