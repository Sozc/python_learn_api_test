# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 14:38
# @Author  : zc
# @Email   : zc_9211@163.com
# @File    : study_reflect.py
# @Software: PyCharm

class People:
    number_eye = 2

    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    p = People('mongo', 18)
    # print(p.number_eye)
    # print(People.number_eye)
    # print(p.name)
    # print(p.age)

    # 查看属性
    print(hasattr(People, "number_leg"))  # 如果有返回True,没有返回False
    print(hasattr(People, "number_eye"))
    # 添加属性(set不判断有没有这个属性，没有就添加，有就修改)
    setattr(People, "number_leg", 2)
    print(hasattr(People, "number_leg"))
    print(People.number_leg)

    # 给实例对象添加属性
    setattr(p, "dance", True)
    print(p.dance)

    # 获取属性（get会判断有没有这个属性，有就获取返回，没有就报错）
    getattr(People,"number_leg")  # 获取类属性
    getattr(p, "dance")           # 获取实例属性

    # 删除属性
    delattr(p, "dance")
    getattr(p, "dance")