### python基础语法



## 数据类型与变量

# print('I\'m ok.')
# print('I\'m learning\nPython.')
# print('\\\n\\')
# print('\\\t\\')
# # 用r''表示''内部的字符串默认不转义
# print(r'\\\t\\')
# # 用'''...'''的格式表示多行内容
# print('''line1
# line2
# line3''')

# print(True)
# print(False)
# print(3>2)
# print(2<1)
#
# # 布尔值可以用and、or和not运算。
# # and运算是与运算，只有所有都为True，and运算结果才是True：
# print(True and True)
# print(True and False)
# print(False and False)
# # or运算是或运算，只要其中有一个为True，or运算结果就是True
# print(True or True)
# print(True or False)
# print(False or False)
# # not运算是非运算，它是一个单目运算符，把True变成False，False变成True
# print(not True)
# print(not False)
# print(not 3>2)

# age = 1
# if age >= 18:
#     print('adult')
# else:
#     print('teenager')
#
# PI=3.14159265359
# print('PI=',PI)
# print("10/3=",10/3)
# print("10//3=",10//3)
# print("9/3=",9/3)
# print("9//3=",9//3)
# print("9%3=",9%3)
# print("10%3=",10%3)




## 字符串与编码
# print("囊中羞涩")
# print(ord('囊'))
# print(chr(22218))
# print(ord('A'))
# print(chr(65))

# print("\u4e2d\u6587") # 中文
# print('ABC'.encode('ascii'))
# print(b'ABC'.decode('ascii'))
# print('中文'.encode('gb2312'))
# print(b'\xd6\xd0\xce\xc4'.decode('gb2312'))
# print('中文'.encode('UTF-8'))
# # 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
# print(b'\xe4\xb8\xad\xe6\x96'.decode('UTF-8',errors='ignore'))

#计算str包含多少个字符，可以用len()函数
# lens = len('ABC')
# print(lens)
# lens = len('中文')
# print(lens)
# lens = len('囊中羞涩')
# print(lens)


## 占位符
# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数
print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

# test
s1=int(input('小明上学期期末成绩为：'))
s2=int(input('小明本学期期末成绩为：'))
r=((s2-s1)/s1*100)
print('小明本次成绩变化为 %.1f%%'%r)