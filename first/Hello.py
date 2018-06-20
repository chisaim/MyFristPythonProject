# -*- coding: utf-8 -*-
#
import keyword
import math

print(keyword.kwlist)

''
""
""" """
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a + b
i = 256 * 256
print()
print('The value of i is', i)
a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))
#  得到一个浮点数
print(2 / 4)
#  得到一个整数
print(2 // 4)
#  得到一个乘方
print(2 ** 4)
#  得到开方就得引入math包了
print(math.sqrt(32))
print('c:\some\name')
print(r'c:\some\name')
print("str" + "ing", "mmm" * 3)
word = "ILovePython"
print(word[0], word[10], len(word))
print(word[-1], word[-11])
print(word[1:5])
print(word[-6:])
a = ['him', 25, 100, 'her']
b = ['hhh', 'wdv', 'grsa', 'his']
print(a + b)
c = a + b
c[0] = 1818
c[2:5] = [17, 18, 20]
print(c)
d = ('www', 133, "for", 4003)
print(d, type(d), len(d))
print(d.__contains__(133))
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)
print('Tom' in student)
a = set('abracadabra')
b = set('alacazam')
#  set无序不重复集合
print(a, b)
#  a和b的差集
print(a - b)
#  a和b的并集
print(a | b)
#  a和b的交集
print(a & b)
#  a和b的逆交集
print(a ^ b)
dic = {'Jack': 1557, 'Tom': 1320, 'Rose': 1886}
print(dic['Jack'], dic['Tom'], dic['Rose'])
del dic['Jack']
print(dic)
dic['Cat'] = 4433
print(dic)
print(sorted(dic))
print('Tom' in dic)
print('Cat' not in dic)
print(dict([('sape', 4433), ('www', 8989), ('sadd', 9090)]))
print({x: x ** 2 for x in (2, 4, 6)})
print(dict(sape=4433, www=8989, sadd=9090))
if True:
    print(True)
elif True:
    print(False)
else:
    print(False)
n = 100
sumq = 0
counter = 1
while counter <= n:
    sumq += counter
    counter += 1
print(sumq)
for i in range(10):
    print(i, end=",")
    break
else:
    print(i)
for i in range(0, 100, 20):
    print(i, end="_")
print()
for i in range(-10, -1000, -20):
    print(i, end="_")

while True:
    pass
