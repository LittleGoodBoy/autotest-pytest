import logging,time
from untils.readYaml import baseConfig
class Handler_object:
    """
    处理器对象相关操作
    """
    def __init__(self):
        """
        定义Logger对象和formatter对象
        """
        self.logger = logging.getLogger(name='Framework') #日志器
        self.logger.setLevel(level=logging.DEBUG)
        fmt_log = '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s'
        self.formatter = logging.Formatter(fmt=fmt_log)
        self.log_time = time.strftime("%Y_%m_%d_")
        self.logger_path=baseConfig.logger_path


    def stream_handel(self):
        '''控制台处理器'''
        stream_handel=logging.StreamHandler()
        stream_handel.setLevel(level=logging.INFO)
        stream_handel.setFormatter(fmt=self.formatter)
        self.logger.addHandler(hdlr=stream_handel)

    def file_handle(self):
        '''文件处理器'''
        file_handel = logging.FileHandler(filename='{0}\{1}.log'.format(self.logger_path,self.log_time))
        file_handel.setLevel(level=logging.INFO)
        file_handel.setFormatter(fmt=self.formatter)
        self.logger.addHandler(hdlr=file_handel)

    def getlog(self):
        self.stream_handel()
        self.file_handle()
        return self.logger

logger = Handler_object().getlog()

# if __name__ == '__main__':
#     logger = Handler_object().getlog()
#     logger.info('1111111')
