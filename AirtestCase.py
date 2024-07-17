import os

from airtest.cli.runner import AirtestCase, run_script
from argparse import *
import shutil
from util.config import *
# from lib.log import logger
from airtest.report.report import simple_report


class XFDAirtestCase(AirtestCase):  # 继承AirtestCase类

    def setUp(self):
        # logger.info("案例开始执行")
        super(XFDAirtestCase, self).setUp()  # 继承父类的setup方法

    def tearDown(self):
        # logger.info("案例执行结束")
        super(XFDAirtestCase, self).tearDown()  # 继承父类的tearDown方法

    def run_air(self, root_dir, device):  # 本方法主要是查找脚本文件，目录文件，初始化AirtestCase所需要的参数，执行脚本，并生成报告
        airlist = []
        for i in range(len(os.listdir(root_dir))):
            if "." not in os.listdir(root_dir)[i]:
                airlist.append(root_dir+"/"+os.listdir(root_dir)[i])

        for f in airlist:  # 循环查找air所在的目录
            print(os.listdir(f))
            for ff in os.listdir(f):
                print(ff)
                if ff.endswith(".air"):  # 以air结尾的文件
                    airName = ff
                    script = os.path.join(f, ff)  # 脚本目录
                    # logger.info(script)
                    log = os.path.join(logpath + '/' + airName.replace('.py', ''))  # 日志目录
                    print(log)
                    # logger.info(log)
                    if os.path.isdir(log):
                        shutil.rmtree(log)  # 清空日志目录文件
                    else:
                        os.makedirs(log)
                    # 初始化父类AirtestCase所需要的参数
                    args = Namespace(device=device, log=log, recording=None, script=script, compress=False, no_image=False)
                    try:
                        run_script(args, AirtestCase)  # 执行air脚本文件
                    except AssertionError:
                        pass
                        # logger.info("案例执行失败")
                    finally:
                        output_file = log + '/' + airName.replace('.py', '') + '.html'
                        # logfile = log + '/' + 'log.txt' logfile=logfile,
                        # output_file = logpath + '\\' + +airName.replace('.air', '') + '.html'  # 生成报告目录
                        simple_report(script, logpath=log, output=output_file)  # 生成报告的方法
                        # logger.info("案例执行成功")


if __name__ == '__main__':
    test = XFDAirtestCase()
    # device = ['Android://127.0.0.1:5037/172.16.81.115:5555']
    test.run_air(airpath, Androiddevice)
