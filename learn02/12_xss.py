# coding:utf-8

from flask import Flask, render_template, request


app = Flask(__name__,
            static_folder="../static",  # 静态文件的目录，默认就是static  加上..相对于整个目录，这里是练习。多了个包
            template_folder="../templates",  # 模板文件的目录，默认是templates
            )


@app.route("/xss", methods=["GET", "POST"])
def xss():
    text = ""
    if request.method == "POST":
        text = request.form.get("text")

    return render_template("xss.html", text=text)


if __name__ == '__main__':
    app.run(debug=True)
