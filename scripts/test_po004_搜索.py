import sys,os,pytest
sys.path.append(os.getcwd())

from Base.InitDriver import init_driver
from Page.Page import Page_Obj
from Base.Read_Data import ret_yaml_data

def test_data():
    data_list = []
    data = ret_yaml_data("search_data").get("Search_Data")
    for i in data.keys():
        data_list.append((i,data.get(i).get("test")))
    return data_list

class Test_search:
    def setup_class(self):

        self.driver = init_driver()

        # 统一页面对象管理类Page_Obj，调用函数Search_Page()
        self.search_obj = Page_Obj(self.driver).Search_Page()

    def teardown_class(self):
        self.driver.quit()

    def test_search01(self):
        # 点击搜索按钮
        self.search_obj.click_search()

    @pytest.mark.parametrize("test_id,data",test_data())
    def test_search02(self,test_id,data):           # 参数必须和parametrize里面的参数一致

        print("用例编号：",test_id)
        # 输入搜索内容
        self.search_obj.input_search(data)
        # 截图
        self.driver.get_screenshot_as_file("./screen/set_%s.png"% data)

    def test_search03(self):
        # 点击返回按钮
        self.search_obj.click_return()

