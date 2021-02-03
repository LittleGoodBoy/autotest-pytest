import unittest
from untils.HttpClient import HttpClientRequest
from untils.readYaml import baseConfig
from untils.op_mysql import execute
from log.log import logger
from ddt import ddt,data,file_data
from untils.op_excel import Excel_rw
from untils.tool import *
apiPre=baseConfig.api['test']
#apicase_path=baseConfig.APICASE_YAML_PATH
apicase_path=baseConfig.APICASE_EXCEL_PATH
@ddt
class TestCaseAPi(unittest.TestCase):
    '''
    作业：驱动excel表格用例，所有的sheet表格，所有的用例依次执行，而且打印接口执行个数
    '''
    index=0
    '''几个接口的用例'''
    #Cases_Info=Excel_rw(filename=apicase_path).read_api_cases() #读取excel所有的用例数据
    Cases_Info=get_api_excel_case()
    @classmethod
    def setUpClass(self) -> None:
        '''所有用例的前置'''
        self.request=HttpClientRequest()

    def tearDown(self) -> None:
        '''接口请求后，初始化headers'''
        self.request.init_headers()

    # @file_data(apicase_path)
    # def test01(self,**caseinfo):
    #     '''
    #     登录
    #     :return:
    #     '''
    #     TestCaseAPi.index+=1
    #     casename,method,apiname,data,extract,duanyan,headers=caseinfo['casename'],caseinfo['method'],\
    #                                                  caseinfo['apiname'],caseinfo['data'],\
    #                                                  caseinfo['extract'],caseinfo['duanyan'],caseinfo['headers']
    #     res=self.request.sendRequest(method=method,
    #                                  name=apiname,
    #                                  data=data,
    #                                  tiqu=extract,
    #                                  headers=headers,
    #                                  index=TestCaseAPi.index)#3.发请求过程
    #     #self.request.validate(yuqi=duanyan, shiji=res)
    #     result=self.request.validate(yuqi=duanyan,shiji=res) #返回元组（1布尔值，2验证信息）
    #     logger.info(result[1])
    #     self.assertTrue(result[0])#4.结果验证
    #     '''拿到响应值,写入到excel，输入到报告'''

    @data(*Cases_Info)
    def test01(self, Case_Info):
        '''
        登录
        :return:
        '''
        print(Case_Info)
        TestCaseAPi.index += 1
        casename, method, apiname, data, extract, duanyan, headers ,host= Case_Info['接口用例名称'], Case_Info['请求方式'], \
                                                                     Case_Info['接口url'], Case_Info['请求入参'], \
                                                                     Case_Info['提取变量'], Case_Info['检查点'], \
                                                                     Case_Info['请求头信息'],Case_Info['域名'],
        #excel里面字典类型数据转化
        data=json_loads(data)
        headers=json_loads(headers)
        duanyan=json_loads(duanyan)
        extract=json_loads(extract)
        url=host+apiname
        res = self.request.sendRequest(method=method,
                                       url=url,
                                       data=data,
                                       tiqu=extract,
                                       headers=headers,
                                       index=TestCaseAPi.index)  # 3.发请求过程
        result = self.request.validate(yuqi=duanyan, shiji=res)  # 返回元组（1布尔值，2验证信息）
        logger.info(result[1])
        self.assertTrue(result[0])  # 4.结果验证
        '''拿到响应值,写入到excel，输入到报告'''


if __name__ == '__main__':
    unittest.main()