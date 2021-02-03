import pytest
from AppTestCase.POM.homepage import HomePage
@pytest.fixture()
def loginapp(openapp):
    # openapp.xpath('//*[@resource-id="com.netease.cloudmusic:id/i7"]').click()#点击登录进入登录页面
    # openapp(text='手机号登录').click()
    # openapp(resourceId='com.netease.cloudmusic:id/a69').send_keys('15902127953')
    # openapp(resourceId='com.netease.cloudmusic:id/f7').send_keys('15902127953')

    openapp.click_my(HomePage.loginButton)
    openapp.click_my(HomePage.shoujihaodenglu)
    openapp.send_key(value='15902127953',loc=HomePage.username)
    openapp.send_key(value='11111111',loc=HomePage.password)