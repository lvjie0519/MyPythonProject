# -*- coding: UTF-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错
# 解决方法为只要在文件开头加入 # -*- coding: UTF-8 -*- 或者 # coding=utf-8 就行了

# 2019.11.30日学习
# print("你好，世界")
#
# word = 'word'
# sentence = "这是一个句子。"
# paragraph = """这是一个段落。
#     包含了多个语句"""
#
# print(word)
# print(sentence)
# print(paragraph)

# 2019.12.15 学习
# 定义变量  del
# var1 = 1
# var2 = {
#     'name': 'lvjie',
#     'age': 23,
#     'email': 'adb.emlal.com'
# }
#
# print var1  # 1
# print var2  # {'age': 23, 'name': 'lvjie', 'email': 'adb.emlal.com'}
#
# del var2['age']
# print var2  # {'name': 'lvjie', 'email': 'adb.emlal.com'}
#
# del var1
# # print var1  # 异常崩溃 name 'var1' is not defined


# 字符串
# str = 'Hello World!'
#
# print str  # 输出完整字符串  Hello World!
# print str[0]  # 输出字符串中的第一个字符  H
# print str[2:5]  # 输出字符串中第三个至第六个之间的字符串 llo
# print str[2:]  # 输出从第三个字符开始的字符串  llo World!
# print str * 2  # 输出字符串两次  Hello World!Hello World!
# print str + "TEST"  # 输出连接的字符串  Hello World!TEST

# 列表--数组
# list = ['runoob', 786, 2.23, 'john', 70.2]
# tinylist = [123, 'john']
#
# print list  # 输出完整列表
# print list[0]  # 输出列表的第一个元素  runoob
# print list[1:3]  # 输出第二个至第三个元素  [786, 2.23]
# print list[2:]  # 输出从第三个开始至列表末尾的所有元素  [2.23, 'john', 70.2]
# print tinylist * 2  # 输出列表两次  [123, 'john', 123, 'john']
# print list + tinylist  # 打印组合的列表  ['runoob', 786, 2.23, 'john', 70.2, 123, 'john']

# Python 元组
# 元组是另一个数据类型，类似于 List（列表）。元组用 () 标识。内部元素用逗号隔开。
# 但是元组不能二次赋值，相当于只读列表。
# tuple = ('runoob', 786, 2.23, 'john', 70.2)
# tinytuple = (123, 'john')
#
# print tuple  # 输出完整元组
# print tuple[0]  # 输出元组的第一个元素
# print tuple[1:3]  # 输出第二个至第四个（不包含）的元素
# print tuple[2:]  # 输出从第三个开始至列表末尾的所有元素
# print tinytuple * 2  # 输出元组两次
# print tuple + tinytuple  # 打印组合的元组
#
# # tuple[2] = 1000    # 元组中是非法应用  'tuple' object does not support item assignment

# Python 字典 -- 键值对
# 字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。
# 两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典用"{ }"标识。字典由索引(key)和它对应的值value组成。

# dict = {}
# dict['one'] = "This is one"
# dict[2] = "This is two"
#
# tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
#
# print dict['one']  # 输出键为'one' 的值  This is one
# # print dict[1]  # 如果输出没有key的value  或抛异常
# print dict[2]  # 输出键为 2 的值  This is two
# print dict  # 输出完整的字典  {2: 'This is two', 'one': 'This is one'}
# print tinydict  # 输出完整的字典  {'dept': 'sales', 'code': 6734, 'name': 'john'}
# print tinydict.keys()  # 输出所有键  ['dept', 'code', 'name']
# print tinydict.values()  # 输出所有值  ['sales', 6734, 'john']

# 学到这里
# https://www.runoob.com/python/python-variable-types.html
