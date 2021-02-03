'''web端用例执行入口'''
import pytest
'''运行所有的web用例'''
#pytest.main(['-s','-vv','--alluredir','./report/xml'])



'''运行某一个文件的用例'''


'''运行所有的app用例'''
pytest.main(['-s','-vv','../zidonghua/AppTestCase','--alluredir','./report/xml'])



