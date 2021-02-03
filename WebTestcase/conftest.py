print('这是webui自动化目录下的conftest，把登录拆分，1.根目录打开了浏览器被测网站2.登录过程')
import pytest,time
from WebTestcase.POM.HomePage import HomePage
from WebTestcase.POM.LoginPage import LoginPage

@pytest.fixture()
def login(openbrowser):
    '''登录过程'''
    # openbrowser.find_element(*HomePage.Login_buttom).click()
    # openbrowser.find_element(*LoginPage.username).send_keys('zhiyi')
    # openbrowser.find_element(*LoginPage.password).send_keys('123456')
    # # 输入验证码
    # time.sleep(9)
    # openbrowser.find_element(*LoginPage.login_button).click()
    # return openbrowser

    openbrowser.click_my(HomePage.Login_buttom)
    openbrowser.send_key_my(LoginPage.username,'zhiyi')
    openbrowser.send_key_my(LoginPage.password,'123456')
    # 输入验证码
    openbrowser.click_my(LoginPage.login_button)
    yield openbrowser

