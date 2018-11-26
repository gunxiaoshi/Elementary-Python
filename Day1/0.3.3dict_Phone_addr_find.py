#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Farr Ding  Time: 2018/7/20

# 一个使用get()的简单数据库
# 一个将人名用作键的字典。每个人都用一个字典表示，
# 字典包含键'phone'和'addr'，它们分别与电话号码和地址相关联
people = {
    'Alice': {
        'phone': '2341',
        'addr': 'Foo drive 23'
        },
    'Beth': {
        'phone': '9102',
        'addr': 'Bar street 42'
        },
       'Cecil': {
        'phone': '3158',
        'addr': 'Baz avenue 90'
        }
    }
# 电话号码和地址的描述性标签，供打印输出时使用
labels = {
    'phone': 'phone number',
    'addr': 'address'
}
name = input('Name: ')
# 要查找电话号码还是地址？
request = input('Phone number (p) or address (a)? ')
# 使用正确的键：
key = request  # 如果request既不是'p'也不是'a'
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'
# 使用get提供默认值
person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, 'not available')
print("{}'s {} is {}.".format(name, label, result))