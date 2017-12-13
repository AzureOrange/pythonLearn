# -*- coding:utf-8 -*-
'''
+ : 合并
* : 复制
in ：元素是否存在
not in : 元素是否不存在
'''

print('ab' * 4)

'''
cmp(item1, item2) 比较两个值 ---3.0 不支持

len(item) 计算容器中元素个数

max(item) 返回容器中元素最大值

del(item) 删除变量
'''

print(len("hello itcast"))

print(max("hello itcast"))

a = 1
del a


# --- 引用 ---

a = 1
print(id(a))

b = a;
print(id(b))  # 跟id(a) 一致

a = 3
print(id(a)) # 变化
print(id(b))

b = 9
print(id(b)) # 变化