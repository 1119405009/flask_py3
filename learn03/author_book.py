# coding:utf-8

from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__,
            static_folder="../static",  # 静态文件的目录，默认就是static  加上..相对于整个目录，这里是练习。多了个包
            template_folder="../templates",  # 模板文件的目录，默认是templates
            )


class Config(object):
    # sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1:3306/flask_test"

    # 设置sqlalchemy自动更跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SECRET_KEY = "doiso7fd89fyd9^(fsd"


app.config.from_object(Config)
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app, use_native_unicode="utf8")


# 定义数据库的模型
class Author(db.Model):
    """作者"""
    __tablename__ = "tbl_authors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    books = db.relationship("Book", backref="author")

    def __repr__(self):  # 查询的时候返回
        return "<Author %r>" % self.name



class Book(db.Model):
    """书籍"""
    __tablename__ = "tbl_books"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey("tbl_authors.id"))

    def __repr__(self):  # 查询的时候返回
        return "<Book %r>" % self.name


# 创建表单模型类
class AuthorBookForm(FlaskForm):
    """作者数据表单模型类"""
    author_name = StringField(label=u"作者", validators=[DataRequired(u"作者必填")])
    book_name = StringField(label=u"书籍", validators=[DataRequired(u"书籍必填")])
    submit = SubmitField(label=u"保存")


@app.route("/", methods=["GET", "POST"])
def index():
    # 创建表单对象
    form = AuthorBookForm()

    if form.validate_on_submit():
        # 验证表单成功
        # 提取表单数据
        author_name = form.author_name.data
        book_name = form.book_name.data
        # 保存数据库
        author = Author(name=author_name)
        db.session.add(author)
        db.session.commit()

        book = Book(name=book_name, author_id=author.id)
        # book = Book(name=book_name, author=author)
        db.session.add(book)
        db.session.commit()

    # 查询数据库
    author_li = Author.query.all()
    return render_template("author_book.html", authors=author_li, form=form)


# post  /delete_book  json
# {"book_id":x}

# @app.route("/delete_book", methods=["POST"])
# def delete_book():
#     """删除数据"""
#     # 提取参数
#     # 如果前端发送的请求体数据是json格式，get_json会解析成字典
#     # get_json 要求前端传送的数据的Content-Type: application/json
#     req_dict = request.get_json()
#     book_id = req_dict.get("book_id")
#
#     # 删除数据
#     book = Book.query.get(book_id)
#     db.session.delete(book)
#     db.session.commit()
#
#     # "Content-Type": "application/json"
#     return jsonify(code=0, message="OK")


# /delete_book?book_id=xx
@app.route("/delete_book", methods=["GET"])
def delete_book():
    """删除数据"""
    # 提取参数
    book_id = request.args.get("book_id")

    # 删除数据
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()

    return redirect(url_for("index"))


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    au_xi = Author(name='我吃西红柿')
    au_qian = Author(name='萧潜')
    au_san = Author(name='唐家三少')
    db.session.add_all([au_xi, au_qian, au_san])
    db.session.commit()

    bk_xi = Book(name='吞噬星空', author_id=au_xi.id)
    bk_xi2 = Book(name='寸芒', author_id=au_qian.id)
    bk_qian = Book(name='飘渺之旅', author_id=au_qian.id)
    bk_san = Book(name='冰火魔厨', author_id=au_san.id)
    db.session.add_all([bk_xi, bk_xi2, bk_qian, bk_san])
    db.session.commit()
    app.run(debug=True)














