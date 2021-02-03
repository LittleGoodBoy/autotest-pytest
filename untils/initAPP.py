import uiautomator2 as ut2
from untils.readYaml import baseConfig
appdata=baseConfig.appdata
picturePath=baseConfig.picturePath
def apptype():
    '''设备初始化
    返回设备
    '''
    d=ut2.connect(appdata['devicesname'])
    d.screen_on()
    d.app_stop(appdata['appname'])
    d.app_clear(appdata['appname'])
    d.app_start(appdata['appname'])
    #d.implicitlt_wait(5)
    return d


class Initapp():
    def __init__(self,d):
        self.d=d #设备

    def until_element_visible(self,loc):
        '''
        定位元素
        :param loc:
        :return:
        '''
        ele = ''
        for key,value in loc.items():
            if key=='xpath':
                '''定位这个元素'''
                ele=self.d.xpath(value)
                #如果超过5秒，wait返回的布尔值
                if not ele.wait(5):
                   self.add_allure_picture()
            elif key=='text':
                ele=self.d(text=value)
                if not ele.exists(timeout=5):
                    self.add_allure_picture()
            elif key == 'resourceId':
                ele = self.d(resourceId=value)
                if not ele.exists(timeout=5):
                    self.add_allure_picture()
        return ele

    def click_my(self,loc):
        ele=self.until_element_visible(loc)
        ele.click()

    def send_key(self, value,loc):
        ele = self.until_element_visible(loc)
        ele.send_keys(value)


    def add_allure_picture(self):
        file_path = picturePath + r'\apptest.jpg'
        self.d.screenshot(file_path)  # 截图app页面
        '''添加到allure报告'''
        with open(file_path, mode='rb') as file:
            f = file.read()
            import allure
            allure.attach(f, 'app错误截图', allure.attachment_type.JPG)
        raise ("等待了5miao没有找到该元素")

