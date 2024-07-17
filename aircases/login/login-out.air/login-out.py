# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)



from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 打开crm
start_app('com.igancao.crm')

# 判断是否登录
# 未登录
if exists(Template(r"tpl1681296909705.png", record_pos=(0.255, -0.429), resolution=(1080, 2400))):
    # 点击验证码登录
    poco("com.igancao.crm:id/tvYan").click()
    # 输入账号
    poco("com.igancao.crm:id/etUsername").set_text('right#bocai')
    # 输入验证码
    poco("com.igancao.crm:id/etPassword").set_text('159357456')
    
    sleep(1.0)
    # 点击登录
    poco("com.igancao.crm:id/btnLogin").click()
    sleep(1.0)
    # assert_equal("实际值", "预测值", "请填写测试点.")

# 已登录
else:
    print('已登录')
# 点击 我的
poco("com.igancao.crm:id/rb4").click()

# 点击 退出账户
poco("com.igancao.crm:id/tvLogout").click()

# 返回桌面
keyevent("HOME")
