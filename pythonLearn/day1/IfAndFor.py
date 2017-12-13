# -*- coding:utf-8 -*-

# if
# if 可以嵌套 if
age = 30

if age >= 18:
    print("我已经成年了")

score = 77

if score >= 90 and score <= 100:
    print('本次考试，等级为A')
elif score >= 80 and score < 90:
    print('本次考试，等级为B')
elif score >= 70 and score < 80:
    print('本次考试，等级为C')
elif score >= 60 and score < 70:
    print('本次考试，等级为D')
elif score >= 0 and score < 60:
    print('本次考试，等级为E')


# 循环

# --- while ---
# 九九乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d*%d=%-2d " % (j, i, i * j), end='')
        j += 1
    print('\n')
    i += 1

name = 'abc'

# ----- for ----
for x in name:
    print(x)
else:
    print("没有数据")

# break和continue

