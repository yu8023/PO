import sys,os,pytest
sys.path.append(os.getcwd())

from Base.InitDriver import init_driver
from Page.add_person import Add_Person
from Base.Read_Data import ret_yaml_data
import allure

# 调用读取yml文件的函数
def read_test_data():
    data_list=[]
    data = ret_yaml_data("add_user").get("User")
    for i in data.keys():
        data_list.append((i,data.get(i).get("name"),data.get(i).get("phone"),data.get(i).get("expect")))

    return data_list

class Test_add():
    def setup_class(self):
        self.driver = init_driver()

        # 实例化二次封装的Add_Person类，把声明的对象丢给Add_Person
        self.add_obj = Add_Person(self.driver)

    def teardown_class(self):
        self.driver.quit()

    # 测试步骤
    @allure.step(title="点击添加联系人按钮")
    @pytest.fixture()
    def add01(self):
        self.add_obj.add_p_btn()
        # print(self.driver.page_source)
        if '本地保存' in self.driver.page_source:
            self.add_obj.click_left_btn()
            print("点击成功")
            return True
        else:
            return False

    @allure.step(title="添加联系人信息")
    @pytest.mark.usefixtures("add01")
    @pytest.mark.parametrize("test_num,name,phone,expect", read_test_data())
    def test_add02(self, test_num, name, phone, expect):
        print("测试用例ID：%s \n期望结果：%s"% (test_num,expect) )
        self.add_obj.input_user_info(name, phone)
        if test_num == "test_user_001":
            assert expect not in self.add_obj.get_user_list()    # ['abc', '丁丁', 'dingding']
        else:
            assert expect in self.add_obj.get_user_list()



