from selenium import webdriver
from untils.readYaml import baseConfig
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from log.log import logger
import allure
def browsertype():
    '''
    根据yaml配置文件，初始化浏览器
    类型，运行环境，用例的url
    :return: 浏览器对象
    '''
    if baseConfig.browser['env']=='docker':
        print('开始启动docker模式')
        chrome_capabilities = {
            "browserName": "chrome",
        }
        driver = webdriver.Remote("http://47.94.172.18:5555/wd/hub", desired_capabilities=chrome_capabilities)
    else:
        options=webdriver.ChromeOptions()#谷歌浏览器的可选项对象
        if baseConfig.browser['env']=='headless':
            options.add_argument('headless')
        if baseConfig.browser['type']=='chrome':
            driver=webdriver.Chrome(options=options,executable_path=baseConfig.chrome_driver_path)
        elif baseConfig.browser['type']=='firefox':
            driver=webdriver.Firefox(executable_path=baseConfig.firefox_driver_path)
        elif baseConfig.browser['type']=='ie':
            driver=webdriver.Ie()
        else:
            raise ('没有支持的浏览器类型{}'.format(baseConfig.browser['type']))
    driver.get(baseConfig.ui['test'])
    driver.save_screenshot('./1024.png')
    driver.maximize_window()#浏览器最大化
    return driver

class BrowserInit():
    '''封装浏览器常用操作：
    等待时间
    log
    错误截图

    '''
    def __init__(self,driver):
        self.driver=driver

    def until_element_visible(self,loc):
        '''等待元素出现'''
        time=8
        try:
            element=WebDriverWait(self.driver,time).until(EC.visibility_of_element_located(loc))
        except Exception as e:
            logger.info('{}个元素超过了8秒未找到'.format(loc[1]))
            self.add_fail_picture()
            raise e
        return element


    def until_elements_visible(self,loc):
        '''一个元素在页面上出现的次数'''
        time=8
        try:
            elements=WebDriverWait(self.driver,time).until(lambda x:x.find_elements(*loc))
        except Exception as e:
            logger.info('{}个元素超过了8秒未找到'.format(loc[1]))
            self.add_fail_picture()
            raise e
        return elements

    def send_key_my(self,loc,value):
        ele=self.until_element_visible(loc)
        logger.info('在{0}：个元素输入了：{1}'.format(loc[1],value))
        ele.send_keys(value)

    def click_my(self,loc):
        ele=self.until_element_visible(loc)
        logger.info('点击了{0}：元素'.format(loc[1]))
        ele.click()


    def add_fail_picture(self):
        '''
        截图，添加到allure的报告里面去
        :return:
        '''
        file_name=baseConfig.picturePath+r'\test.jpg'
        self.driver.save_screenshot(file_name)  # 截图函数
        '''allure添加截图附件'''
        with open(file_name, mode='rb') as file:
            f = file.read()  # 读取文件，将读取的结果作为参数传给allure
        allure.attach(f, 'denglu', allure.attachment_type.JPG)

    def element_visible_times(self,loc):
        '''验证结果方法'''
        return len(self.until_elements_visible(loc))

    # def execute_js(self):
    #     js='documet.get().style'
    #     self.driver.execute_javascript()

    '''切换窗口'''
    '''鼠标移动'''



if __name__ == '__main__':
    browsertype()