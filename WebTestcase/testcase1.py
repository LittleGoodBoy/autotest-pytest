'''需要登录：购物车模块的用例'''
from untils.initBrowser import browsertype
from WebTestcase.POM.HomePage import HomePage

# import time
# class TestLogin():
# #     def test01(self,login):
# #         '''用例：登录之后，'''
# #         print('111')
#         # login.send_key_my(HomePage.gouwuche).click()
#
#         # time.sleep(5)
#         #'''购物车的增删改查'''
#     #
#     def test02(self,login):
#         '''购物车结算界面：
#         1.点击结算
#         2.根据提示是否需要勾选商品
#             一般弹出的提示：这个元素在页面肯定存在，根据元素的属性是否显示
#         '''
#         login.find_element_by_xpath(*HomePage.gouwuche).click()
#         #获取弹窗的属性
#         time.sleep(5)


'''
1.在执行操作过程中，如果有错误，添加allure报错错误截图
2.封装一层业务关键字，搜索
前台：http://shopxo.hctestedu.com/
后台http://shopxo.hctestedu.com/admin.php
用户名：admin mima :shopxo
'''