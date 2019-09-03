#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   models.py    
@Contact :   1119405009@qq.com
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/9/3 12:02   felix      1.0         None
'''
# import lib

from flask_login import UserMixin

class User(UserMixin):
    pass

users = [
    {'id':'Tom', 'username': 'Tom', 'password': '111111'},
    {'id':'Michael', 'username': 'Michael', 'password': '123456'}
]

def query_user(user_id):
    for user in users:
        print(user)
        print(user['id'])
        print(user_id == user['id'])
        if user_id == user['id']:
            return user
