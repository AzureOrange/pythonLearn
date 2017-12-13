# -*- coding:utf-8 -*-
# 字符串可以用单引号或者双引号表示
name = "hello iTcast.cn"
name = 'hello iTcast.cn'
print("职位：%s" % name)
print(name[2])
print(name[0:3])  # 取 下标0~2 的字符
print(name[2:])  # 取 下标为2开始到最后的字符
print(name[1:-1])  # 取 下标为1开始 到 最后第2个之间的字符

print(name.find("l", 1, 12))
print(name.index("l", 1, 12))  # 跟find()方法一样，只不过如果str不在name中会报一个异常.
name.rindex("l", 1, 12)  # 类似index  只不过从右边开始
print(name.count("l", 1, 12))

name = name.replace("l", "A", 1)  # 把 name 中的 l 替换成 A,如果 count 指定，则替换不超过 count 次.
print(name)

name.split(" ", 3)

name.capitalize()  # 把字符串的第一个字符大写

name.title()  # 把字符串的每个单词首字母大写

name.startswith("h")  # 检查字符串是否是以 h 开头, 是则返回 True，否则返回 False
name.endswith("h")

name.lower()  # 所有大写字符为小写
name.upper()  # 小写字母为大写


# 对齐
name.ljust(10)  # 返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
name.rjust(10)
name.center(10)  # 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串

name.lstrip()  # 删除左边的空白字符
name.rstrip()
name.strip()  # 删除两端的空白

name.partition("A")  # 以分割成三部分,str前，str和str后
name.rpartition("A")  # 类似于 partition()函数,不过是从右边开始.

name.splitlines()  # 按照行分隔"\n"，返回一个包含各行作为元素的列表

# 判断
name.isalpha()  # 所有字符都是字母 则返回 True,否则返回 False

name.isdigit()  # 只包含数字则返回 True 否则返回 False.

name.isalnum()  # 所有字符都是字母或数字则返回 True,否则返回 False

name.isspace()   # 只包含空格，则返回 True，否则返回 False.

str = " "
li = ["A", "B", "C"]
print(str.join(li))  # 每个字符后面插入str,构造出一个新的字符串


# ------- 列表 ------
# 列表中存放的数据是可以进行修改的，比如"增"、"删"、"改""
namesList = ['AA', 'BB', 'CC', 'AA']
nameCopy = ["1", "2"]
print(namesList[0])

for name in namesList:  # 循环
    print("For循环%s" % name)

length = len(namesList)
i = 0
while i < length:  # 循环
    print(namesList[i])
    i += 1

# 添加
namesList.append("DD")
namesList.extend(nameCopy)
namesList.insert(1, "QQ")
#  修改
namesList[0] = "zhou"
# 判断
'''
in（存在）,如果存在那么结果为true，否则为false
not in（不存在），如果不存在那么结果为true，否则false
'''

# 查询
namesList.index("QQ", 1, 12)
namesList.count("QQ")

# 删除
'''
del：根据下标进行删除
pop：删除最后一个元素
remove：根据元素的值进行删除
'''
del namesList[1]
namesList.pop(2)
namesList.remove("AA")

#  排序
namesList.reverse()  # 逆置
namesList.sort(reverse=True)  # 参数reverse=True可改为倒序，由大到小。

# 列表内的嵌套
schoolNames = [['北京大学', '清华大学'],
               ['南开大学', '天津大学', '天津师范大学'],
               ['山东大学', '中国海洋大学']]

# -----元组----
# Python的元组与列表类似，不同之处在于元组的元素不能修改。元组使用小括号，列表使用方括号。
aTuple = ('A', 1, 2.9)
# 访问元组
print(aTuple[0])

aTuple.index("A")
aTuple.count("A")

# ----- 字典 --
studenDict = {'name':'班长', 'id': 100, 'sex':'f', 'address':'地球亚洲中国北京'}

# 查询
print(studenDict['name'])
# 修改
studenDict['name'] = "帅气"
# 增加
studenDict['age'] = 12
# 删除
'''
del  删除整个字典
clear() 清空整个字典
'''

age = studenDict.get('age')
print(age)

# 常用操作
len(studenDict)
studenDict.keys()
studenDict.values()
studenDict.items()
# studenDict.has_key('name')  # 如果key在字典中，返回True，否则返回False

# 遍历
# 通过for ... in ...:的语法结构，我们可以遍历字符串、列表、元组、字典等数据结构。

# 字符串遍历
a_str = "hello itcast"
for char in a_str:
    print(char, end=' ')

# 列表遍历
a_list = [1, 2, 3, 4, 5]
for num in a_list:
    print(num, end=' ')

# 元组遍历
a_turple = (1, 2, 3, 4, 5)
for num in a_turple:
    print(num, end=" ")

# 字典遍历
for key in studenDict.keys():
    print(key)

for value in studenDict.values():
    print(value)

for key, value in studenDict.items():
    print('key = %s And Value = %s'% (key, value))

chars = ['a', 'b', 'c', 'd']

for i, chr in enumerate(chars):
    print(i, chr)
