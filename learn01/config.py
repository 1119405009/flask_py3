#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   config.py
@Contact :   1119405009@qq.com
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/8/23 9:21   felix      1.0         None
'''
# import lib
from flask import Flask, current_app, render_template

# 创建flask的应用对象
# __name__表示当前的模块名字
#           模块名，flask以这个模块所在的目录为总目录，默认这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__,
            static_folder="../static",  # 静态文件的目录，默认就是static  加上..相对于整个目录，这里是练习。多了个包
            template_folder="../templates",  # 模板文件的目录，默认是templates
            )


# 配置参数的使用方式
# 1. 使用配置文件
app.config.from_pyfile("config.cfg")

# 2. 使用对象配置参数
class Config(object):
    DATE = "python"

#注入config对象
app.config.from_object(Config)

@app.route("/")
def index():
    """定义的视图函数"""
    # a = 1 / 0
    # 读取配置参数
    # 1. 直接从全局对象app的config字典中取值
    print(current_app.config.get("DATE"))
    # 2. 通过current_app获取参数
    print(current_app.config.get("DEBUG"))
    return "hello flask"


if __name__ == '__main__':
    # 启动flask程序
    # app.run()
    app.run(host="0.0.0.0", port=5000, debug=True)