# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

start_app('com.igancao.crm')
sleep(1.0)

# 判断是否登录
# 未登录
if poco("com.igancao.crm:id/tvYan"):
    # 点击验证码登录
    poco("com.igancao.crm:id/tvYan").click()
    # 输入账号
    poco("com.igancao.crm:id/etUsername").set_text('tester')
    # 输入验证码
    poco("com.igancao.crm:id/etPassword").set_text('password')

    sleep(1.0)
    # 点击登录
    poco("com.igancao.crm:id/btnLogin").click()
    sleep(1.0)
    # assert_equal("实际值", "预测值", "请填写测试点.")

# 已登录
else:
    print('已登录')
sleep(3)
# 点击底部医生tab
poco('com.igancao.crm:id/rb2').click()

assert_equal(poco('com.igancao.crm:id/tvTitle').get_text(), '我的医生', '是否进入我的医生页面')

# 找到医生熊大
doctor_name = '熊大'
try:
    check_list =[]
    # 首页列表寻找医生：熊大
    while not poco(text=doctor_name):
        # 找到当前页面总条数
        items = poco("com.igancao.crm:id/tvName")
        nums = len(items)

        # 没找到则加载数据poco("<Root>")
        poco("com.igancao.crm:id/wmv").swipe([-0.025, -0.5])
        
            
        latest_doctor_name = items[-1].get_text()
        
        check_list.append(latest_doctor_name)
        
        print(check_list)
        
        if len(check_list) >=2 and check_list[-1] == check_list[-2]:
            break

    # 找到医生后点击医生头像
    poco(text=doctor_name).click()
    sleep(1.0)
    
    # 断言医生姓名是否一致
    assert_equal(poco('com.igancao.crm:id/tvName').get_text(),doctor_name,'校验医生姓名是否一致')
    # 点击进入医生详情
    poco("com.igancao.crm:id/ivNext").click()
    # 断言医生详情内姓名展示是否一致
    assert_equal(poco('com.igancao.crm:id/tvName').get_text(), doctor_name, "校验医生详情姓名是否一致.") 
    
except:
    print("不存在医生："+doctor_name)
# 返回到我的医生页面
while poco('com.igancao.crm:id/tvBack'):
    poco('com.igancao.crm:id/tvBack').click()

assert_equal(poco('com.igancao.crm:id/tvTitle').get_text(), '我的医生', '是否进入我的医生页面')    
# 切换到代理医生
poco("com.igancao.crm:id/tvTitle").click()
poco("com.igancao.crm:id/tvProxyDoctors").click()
assert_equal(poco('com.igancao.crm:id/tvTitle').get_text(), '代理医生', '是否进入代理医生列表')  
# 切换到区域医生
poco("com.igancao.crm:id/tvTitle").click()
poco("com.igancao.crm:id/tvAreaDoctor").click()
assert_equal(poco('com.igancao.crm:id/tvTitle').get_text(), '区域医生', '是否进入区域医生列表')  
# 切换到团队医生
poco("com.igancao.crm:id/tvTitle").click()
poco("com.igancao.crm:id/tvGroup").click()
assert_equal(poco('com.igancao.crm:id/tvTitle').get_text(), '团队医生', '是否进入团队医生列表')  
# 切换回我的医生列表
poco("com.igancao.crm:id/tvTitle").click()
poco("com.igancao.crm:id/tvMyDoctor").click()

# 点击排序按钮
poco("com.igancao.crm:id/ivRight").click()

# 选择排序方式
poco(text="注册时间从近到远").click()

# 点击搜索按钮
poco("com.igancao.crm:id/ivSearch").click()

# 判断是否进入搜索页面
assert_equal(poco("com.igancao.crm:id/etContent").get_text()
, "请输入医生姓名、手机号、医院名称", "是否进入搜索页面")

# 输入搜索关键词
poco("com.igancao.crm:id/etContent").set_text('熊大')

# 点击搜索按钮
poco("com.igancao.crm:id/tvSure").click()

# 搜索结果
if poco("com.igancao.crm:id/tv"):
    poco("com.igancao.crm:id/tv").click()
    sleep(2)
    poco("com.igancao.crm:id/tvBack").click()


stop_app('com.igancao.crm')
