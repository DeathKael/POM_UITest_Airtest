# -*- coding: utf-8 -*
import os

Androiddevice = ["Android://127.0.0.1:5037"]  # 连接安卓设备127.0.0.1:5037固定写法172.16.81.115安卓真机的Ip
airpath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'aircases')  # 脚本目录
logpath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'log')  # 日志目录
templatepath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'templates')  # 模板目录
reportpath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'report')  # 报告目录
datapath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')  # 测试数据目录
