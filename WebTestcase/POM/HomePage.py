from selenium.webdriver.common.by import By
import pytest

class HomePage():
    '''
    管理页面所有的元素（定位方式，元素的值）
    管理操作这些元素的方法
    '''
    search_input=(By.ID,'search-input')
    Login_buttom=(By.XPATH,"//*[text()='登录'  and @class='am-btn-primary btn am-fl']")
    search_button=(By.ID,'ai-topsearch')
    gouwuche=(By.XPATH,'')

    sousuojieguo=(By.CLASS_NAME,'am-animation-scale-up') #搜索结果的元素

    def sosuo(self,openbrowser,value):
        openbrowser.send_key_my(HomePage.search_input, value)
        openbrowser.click_my(HomePage.search_button)