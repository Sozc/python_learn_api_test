# -*- coding: utf-8 -*-
# @Time    : 2020/5/15 16:39
# @Author  : zc
# @Email   : zc_9211@163.com
# @File    : human_vs_pc.py
# @Software: PyCharm

# 人和机器猜拳游戏
# 选择角色1 曹操 2张飞 3 刘备
# 角色猜拳1剪刀 2石头 3布 玩家输入一个1-3的数字
# 电脑出拳 随机产生1个1-3的数字，提示电脑出拳结果，本局对战结果...赢...输,是否继续？y/n
# 输出结果 角色赢几局 电脑赢几局，平局几次 游戏结束
import random

role_dict = {'1': '曹操', '2': '张飞', '3': '刘备'}
fist_dict = {'1': '剪刀', '2': '石头', '3': '布'}
win = 0
lose = 0
draw = 0

# 选择角色
while True:
    role_num = input('请输入你要选择的角色 1、曹操 2、张飞 3、刘备 ')
    if role_num in ['1', '2', '3']:
        role_name = role_dict[role_num]
        print('玩家选择了{}'.format(role_name))
        break
    else:
        print('角色选择只能输入1/2/3')
        continue
while True:
# 角色出拳
    while True:
        hum_fist_num = input('请出拳 1、剪刀 2、石头 3、布 ')
        if hum_fist_num in ['1', '2', '3']:
            hum_fist_value = fist_dict[hum_fist_num]
            print('玩家出拳：{}'.format(hum_fist_value))
            break
        else:
            print('出拳选择只能输入1/2/3')
            continue

    # pc出拳
    pc_fist_num = random.randint(1, 3)  # 产生的整数
    print('pc出拳为：{}'.format(fist_dict[str(pc_fist_num)]))

    # 对战
    # human 赢
    # human 1 -> pc 3 -2
    # human 2 -> pc 1  1
    # human 3 -> pc 2  1

    # pc 赢
    # human 1 -> pc 2 -1
    # human 2 -> pc 3 -1
    # human 3 -> pc 1  2
    if int(hum_fist_num) - pc_fist_num in [-2, 1]:
        # human赢
        print('{}赢了！'.format(role_name))
        win += 1
    elif int(hum_fist_num) - pc_fist_num in [-1, 2]:
        # pc赢
        print('pc赢了！')
        lose += 1
    else:
        print('平局')
        draw += 1
    choice = input('是否要继续？ n 退出 任意键继续')
    if choice == 'n':
        break
    else:
        continue
print('玩家胜利{}次，电脑胜利{}次，平局{}次'.format(win, lose, draw))
