'''接口自动化用例执行入口
unittest+htmltestrunner+ddt
'''
from lib.HTMLTestRunner import HTMLTestRunner
from untils.readYaml import baseConfig
from InterfaceTestcase.testcase import TestCaseAPi
import unittest,os



def creatsuite():
    '''添加测试集'''
    testunit = unittest.TestSuite()
    test_dir=baseConfig.InterFace_PATH
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="*.py",
                                                   top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTest(test_case)
    return testunit

if __name__ == '__main__':

    # suite=unittest.TestSuite()
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCaseAPi))

    suite=creatsuite() #创建测试套件
    file_name=r'{}\api_report.html'.format(baseConfig.API_REPORT_PATH)
    f=open(file_name,'wb')
    runner=HTMLTestRunner(stream=f,title='华测接口自动化项目',description='xx模块')
    runner.run(suite)
