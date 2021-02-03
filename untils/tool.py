'''
公共方法封装
'''
import datetime
import json
import random
import socket
import time
import hashlib
from untils.op_excel import Excel_rw
from untils.readYaml import baseConfig


def json_loads(data):
    '''excel表填写的字典读取的时候是字符串类型，
        可能包含了空格
      本是字典类型的，没有填写数据的，返回为None
      eval:执行一个字符串表达式，返回表达式的值
    '''
    if data and isinstance(data,str):
        #data=json.loads(data)
        data=eval(data)
    else:
        data=None
    return data
def get_host():
    """
    获取运行主机host
    :return:
    """
    ip = socket.gethostbyname(socket.gethostname())
    return str(ip)


def get_host_port():
    """
    获取运行主机host+port
    :return:
    """
    ip = get_host()
    return "{}:7000".format(ip)
    # return "99.48.58.31:7000"


def get_current_time():
    """
    获取当前时间，返回YYYY-mm-dd HH:MM:SS格式的时间字符串
    """
    return str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


def generate_phone(top=None):
    # 第二位数字
    if top:
        phone = str(top) + "".join(random.choice("0123456789") for _ in range(8))
    else:
        second = [3, 4, 5, 7, 8][random.randint(0, 4)]
        #第三位数字
        third = {3: random.randint(0, 9),
                 4: [5, 7, 9][random.randint(0, 2)],
                 5: [i for i in range(10) if i != 4][random.randint(0, 8)],
                 7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
                 8: random.randint(0, 9), }[second]

        # 最后八位数字
        suffix = random.randint(9999999, 100000000)
        # 拼接手机号
        phone="1{}{}{}".format(second, third, suffix)
    return phone


def generate_idcard():
    """
生成身份证号，生成规则同真实身份证，18位，最后一位可以是数字或者X
    :return:身份证号
    """
    ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
    LAST = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')

    u''' 随机生成新的18为身份证号码 '''
    t = time.localtime()[0]

    first_list = ['362402', '362421', '362422', '362423', '362424', '362425', '362426', '362427', '362428', '362429',
                  '362430', '362432', '110100', '110101', '110102', '110103', '110104', '110105', '110106', '110107',
                  '110108', '110109', '110111', '320101', '320102', '320103', '320104', '320105', '320106']

    x = '%06d%04d%02d%02d%03d' % (int(random.choice(first_list)),
                                  random.randint(t - 50, t - 19),
                                  random.randint(1, 12),
                                  random.randint(1, 28),
                                  random.randint(1, 999))

    y = 0
    for i in range(17):
        y += int(x[i]) * ARR[i]

    id_card = '%s%s' % (x, LAST[y % 11])
    return id_card

def md5(data):
    string = json.dumps(data).replace(': ', ':').replace(', ', ',')
    m = hashlib.md5()
    m.update(string.encode(encoding='utf-8'))
    return m.hexdigest()


def get_api_excel_case():
    '''[{0},{1},{2}]变成[{2}]'''
    runAPI=baseConfig.runAPI
    runAPIs=baseConfig.runAPIS
    casesInfo=Excel_rw(filename=baseConfig.APICASE_EXCEL_PATH).read_api_cases()  # 读取excel所有的用例数据
    if runAPI:
        casesInfo=casesInfo[runAPI-1:runAPI]
    if runAPIs: #[1,3,5]
        cases=[]
        for i in runAPIs:
            cases.append(casesInfo[i-1])
        casesInfo=cases
    return casesInfo


if __name__ == '__main__':
    #print(get_host())
    #print(get_host_port())
    #print(get_current_time())
    #print(generate_phone())
    #print(generate_idcard())
    #print(md5(123))
    print(get_api_excel_case())
