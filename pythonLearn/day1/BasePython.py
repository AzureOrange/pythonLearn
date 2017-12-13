# -*- coding:utf-8 -*-

# 单行注释，可以在里写一些功能说明之类的哦
print('hello world')

# 多行注释
'''我是多行注释，可以写很多很多行的功能说明
    这就是我牛X指出

    哈哈哈。。。
'''
print('你好')


# 变量

num1 = 100  # num1就是一个变量，就好一个小菜篮子

num2 = 87  # num2也是一个变量

result = num1 + num2  # 把num1和num2这两个"菜篮子"中的数据进行累加，然后放到 result变量中

'''
1. Numbers: int long float complex

2. Boolean

3. String

4. List 列表

5. Tuple 元祖

6. Dictionary 字典
'''

# 标示符 ： 由字母、下划线和数字组成，且数字不能开头

age = 10
age += 1
print("我今年%d岁"%age)

name = "xiaohua"
print("我的姓名是%s,年龄是%d"%(name,age))


# 在输出的时候，如果有\n那么，此时\n后的内容会在另外一行显示

#  输入

# password = input("请输入密码:")  # 3.0之前raw_input()也支持
# print ('您刚刚输入的密码是:', password)

'''
算术运算符:
    // : 取整除
    %  : 取余
    ** ：幂
    
复合赋值运算符
    +=   -=  *=  /=  %=  **=  //=
    
比较关系运算符
    ==
    !=
    <>
    and  or  not

'''

# 数据类型转换
'''
int(x [,base ])  long(x [,base ])  float(x )  
complex(real [,imag ])  创建一个复数
str(x)  将对象 x 转换为字符串
repr(x )  将对象 x 转换为表达式字符串
eval(str ) 用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s )  将序列 s 转换为一个元组
list(s )  将序列 s 转换为一个列表
chr(x )  将一个整数转换为一个字符
unichr(x )  将一个整数转换为Unicode字符
ord(x )  将一个字符转换为它的整数值
hex(x )  将一个整数转换为一个十六进制字符串
oct(x )  将一个整数转换为一个八进制字符串
'''



