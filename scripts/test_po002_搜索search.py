import sys,os,pytest
sys.path.append(os.getcwd())

from Base.InitDriver import init_driver
from Page.search import Search_Page

class Test_search:
    def setup_class(self):
        self.driver = init_driver()

        # 实例化二次封装的Search_Page类，把声明的对象丢给Search_Page
        self.search_obj = Search_Page(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize("data",[1,2,3])
    def test_po002(self,data):          # 参数必须和parametrize里面的参数一致
        self.search_obj.search_text(data)
