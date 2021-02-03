'''不用登录：搜索模块'''
import time
from WebTestcase.POM.HomePage import HomePage
from untils.op_mysql import execute
class TestUser(HomePage):
    # def test01(self,openbrowser):
    #     openbrowser.find_element(*HomePage.search_input).send_keys("包包")
    #     openbrowser.find_element(*HomePage.search_button).click()
    #     time.sleep(5)
    def setup(self):
        print('前置')
        self.data=execute('select * from user limit 5')

    def test01(self,openbrowser):
        # openbrowser.send_key_my(HomePage.search_input,'包包')
        # openbrowser.click_my(HomePage.search_button)
        # time.sleep(5)
        # times=openbrowser.element_visible_times(HomePage.sousuojieguo)
        # print('出现的次数{}'.format(times))
        # assert times==2
        print('执行用例前，数据库获取的数据',self.data)
        self.sosuo(openbrowser,value='包包') #业务层关键字


    # def test02(self,openbrowser):
    #     openbrowser.find_element(*HomePage.search_input).send_keys("口红")
    #     openbrowser.find_element(*HomePage.search_button).click()
    #     time.sleep(5)
