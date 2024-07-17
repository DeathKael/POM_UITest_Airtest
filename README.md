# 项目介绍
1.项目基于airtest， 可将IDE编写好的脚本批量执行，批量连接设备执行，并产出测试报告
## 项目配置
### 安装requirements.txt的项目依赖
 ```cd airtest_uitest
pip install -r requirements.txt 
```
### 运行项目
 ```
cd airtest_uitest
// 批量执行脚本（单设备）
python AirtestCase.py
// 多设备执行脚本（单脚本多设备）
python run.py
 ```

### 项目结构
1. airtcases  用例文件.air .py
  a. doctor
  b. ...
  c. ...
2. data 数据文件
3. log 日志文件
4. report 报告文件
5. util
  a. config.py 配置文件
6. AirtestCase.py 多脚本批量执行脚本
7. run.py 多设备执行脚本
8. requirements.txt 依赖包目录
 
### air 脚本的开发
通过airtest工具，开发脚本，可以录制，也可以自己编写，请参考源文档
https://airtest.doc.io.netease.com/


