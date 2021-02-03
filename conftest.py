print('根目录的conftest,所有用例执行之前,初始化浏览器，')
from untils.initBrowser import browsertype, BrowserInit
import pytest, time


@pytest.fixture()
def openbrowser():
    '''初始化浏览器方法'''
    # driver=browsertype()#返回浏览器对象
    # return driver

    driver = browsertype()
    browser = BrowserInit(driver)
    yield browser
    '''yield关键字唤醒teardown操作，清除数据，还原操作'''
    print('所有用例执行完毕,后置操作')
    driver.quit()


from untils.initAPP import apptype, Initapp


@pytest.fixture()
def openapp():
    '''初始化app'''
    # app=apptype()
    # yield app

    app = Initapp(apptype())
    yield app