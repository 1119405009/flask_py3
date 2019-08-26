# coding:utf-8

from flask import Flask, render_template


app = Flask(__name__,
            static_folder="../static",  # 静态文件的目录，默认就是static  加上..相对于整个目录，这里是练习。多了个包
            template_folder="../templates",  # 模板文件的目录，默认是templates
            )


@app.route("/index")
def index():
    data = {
        "name": "python",
        "age": 18,
        "my_dict": {"city": "sz"},
        "my_list": [1, 2, 3, 4, 5],
        "my_int": 0
    }
    return render_template("index.html", **data)


def list_step_2(li):
    """自定义的过滤器"""
    return li[::2]


# 注册过滤器
app.add_template_filter(list_step_2, "li2")


@app.template_filter("li3")
def list_step_3(li):
    """自定义的过滤器"""
    return li[::3]


if __name__ == '__main__':
    app.run(debug=True)
