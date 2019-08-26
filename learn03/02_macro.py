# coding:utf-8

from flask import Flask, render_template, flash


app = Flask(__name__,
            static_folder="../static",  # 静态文件的目录，默认就是static  加上..相对于整个目录，这里是练习。多了个包
            template_folder="../templates",  # 模板文件的目录，默认是templates
            )

flag = True

app.config["SECRET_KEY"] = "SDHFOSDF"


@app.route("/")
def index():
    global flag
    print(flag)
    #if flag:
        # 添加闪现信息
    flash("hello1")
    flash("hello2")
    flash("hello3",category='message')
     #   flag = False


    return render_template("macro_input.html")


if __name__ == '__main__':
    app.run(debug=True)
