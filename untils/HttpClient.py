from untils.op_excel import Excel_rw
import requests
from untils.readYaml import baseConfig
from  log.log import logger
from untils.op_mysql import execute
import json
from untils.tool import *
tiqu_path=baseConfig.TIQU_PATH
class  HttpClientRequest():
    def __init__(self,urlPre=None):
        self.session=requests.session()     #创建session,跨接口请求，统一会话管理
        self.urlPre=urlPre
        self.headers={
            "Content-Type": "application/json",
        }#默认的headers
        self.init_headers()
        self.ex = Excel_rw(filename=tiqu_path)

    def init_headers(self,headers=None):
        '''初始化headers，设置headers为 "application/json"'''
        self.session.headers.update(self.headers)
        self.session.auth = ("admin", 'huace123456')
        #self.session.cookies.update(cookie)
        if headers:
            self.session.headers.update(headers) #headers添加 token

    def zhuanhua(self,data):
        '''
        替换入参中包含了变量的参数
        如果变量以美元符号开头，去调用tool文件里面的封装的方法
        :return:{"username":"admin","password":"$generate_phone"}
        '''
        for key,value in data.items():
            if isinstance(value,str) and value.startswith("{{") and value.endswith("}}"):
                name=value.split("{{")[1].split("}}")[0]
                tiqu_value=self.ex.read_tiqu(name)
                data[key]=tiqu_value #替换参数中带有{{的值，data['topic_id']='5f78728bc3ba1963d844b6e0'
            #select username from user limit 1
            if value.startswith("select") and 'from' in value:
                self.res = execute(value)[0][0]
                data[key]=self.res
            if value.startswith('$'):
                v=value.split("$")[1]
                if v=='generate_phone':
                    res=generate_phone()#随机手机号码方法
                    data[key]=res
        return data
    def validate(self,yuqi,shiji,msg='验证结果'):
        '''
        断言  ：支持多个值的断言，支持校验值是字典，
        待开发，整个返回值可能是list，值是list
        参数1：预期{"token":"huacetest","msg":"success"，'info': {'name': 'admin'},}
         参数2 实际结果

          {'adress': {'city': 'changsha'},
          'httpstatus': 200,
          'info': {'age': 18, 'name': 'admin'},
           'msg': 'success',
           'token': 'huacetest'}
        :return: 布尔值
        '''
        for key,value in yuqi.items():
            #直到预期结果不等于实际结果，才返回False
            if key not in shiji:
                msg+='{}根本不在实际结果里面'.format(key)
                return False,msg
            else:
                if isinstance(value,dict) and isinstance(shiji[key],dict):
                        #{'name': 'admin'}预期
                        #{'age': 18, 'name': 'admin'}#实际
                        #递归
                        res=self.validate(value,shiji[key])
                        if res[0] is False:
                            return res
                elif  value != shiji[key]:
                    msg+='这个{}的值预期是:{},而实际返回的是:{}'.format(key,value,shiji[key])
                    print(msg)
                    return False,msg
        return True,msg

    def sendRequest(self,method,url,index,**kwargs):
        #print(kwargs)
        '''请求之前的判断：1.是否传了参数'''
        data=None
        if "data" in kwargs:
            data=kwargs["data"] #定义了一个变量，入参
            '''请求之前：含有变量的参数的转化'''
            data=self.zhuanhua(data)
        #url=self.urlPre+name
        logger.info("开始请求第{2}个接口,url:{0},入参:{1}".format(url,data,index))

        if "headers" in kwargs and kwargs['headers'] is not None:
            '''表示请求的该接口非json类型,比如是表单类型'''
            h=kwargs["headers"]
            self.init_headers(headers=h)
        else:
            data=json.dumps(data)#将字典类型的参数转化为json字符串
        res=self.session.request(method=method,
                                 url=url,data=data,
                                 params=data)  #真正所有接口发送请求的入口
        logger.info(res.request.headers) #请求头所有信息
        logger.info(res)
        respone=res.json() #转化成字典之后，响应值
        '''2.请求之后 a:提取变量 b.断言 c.连接数据库
        extract={"exToken":"token","zhuangtaima":"httpstatus"}
                {"authorId":{"data":"author_id"}}
        '''
        if 'tiqu' in kwargs and  kwargs['tiqu'] is not None : # 你想要提取变量，
            extract=kwargs['tiqu']#{"topicID":"topic_id"}
            for key,value in extract.items(): #循环需要提取的值，以及命名
                if isinstance(value,str):
                    if value=='token':  #提取变量中，token单独处理
                        headers_token={"token":respone[value]}
                        #self.init_headers(headers=di)
                        self.session.headers.update(headers_token) #之前的session headers添加key
                    else:  #提取的变量，存到一个文件，给下面的接口用
                        #调用一个封装好写入excel文件的方法
                        self.ex.write_tiqu(key,respone[value])
                elif isinstance(value,dict):
                    for _key,_value in value:
                        self.ex.write_tiqu(key,respone[_key][0][_value])


        logger.info("接口请求的头部信息{}".format(res.request.headers))
        logger.info("接口请求完成，响应值{}".format(respone))
        '''断言'''
        #ass=self.validate(duanyan,respone)   #布尔值
        return respone