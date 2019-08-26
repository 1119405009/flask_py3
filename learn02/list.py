#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   list.py    
@Contact :   1119405009@qq.com
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/8/23 11:56   felix      1.0         None
'''
# import lib

data = {
    "name": "python",
    "age": 18,
    "my_dict": {"city": "sz"},
    "my_list": [1, 2, 3, 4, 5],
    "my_int": 0
}
print(data.get("my_list")[::4])