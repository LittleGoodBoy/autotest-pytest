'''场景：用例执行之前，连接数据库，查前置数据'''
import pymysql
from untils.readYaml import baseConfig
database=baseConfig.database
class Exe_SQL():
    def __init__(self,username,password,dbname,serve):
        self.username=username
        self.password = password
        self.dbname = dbname
        self.serve = serve


    def exce_sql(self,sql):
        db_connect=pymysql.connect(host=self.serve,
                                   port=3307,
                                   user=self.username,
                                   passwd=self.password,
                                   charset='utf8',
                                   database=self.dbname,
                                   autocommit=True)
        cursor=db_connect.cursor()
        result=''
        try:
            cursor.execute(sql)
            result=cursor.fetchall()
        except Exception as e:
            print(e)
        db_connect.close()
        return result

def execute(sql):
    connet=Exe_SQL(username=database['username'],
                   password=database['password'],
                   dbname=database['dbname'],
                   serve=database['serve'])
    res=connet.exce_sql(sql)
    return res

if __name__ == '__main__':
    res=execute('select * from user limit 5')
    print(len(res),res)