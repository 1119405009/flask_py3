# coding:utf-8

from flask import Blueprint


app_cart = Blueprint("carts", __name__, template_folder="templates")
#D:\py\flask_py3\learn04\cart\views.py
# cart.app_cart
import learn04.cart.views