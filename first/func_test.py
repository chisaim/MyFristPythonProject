# def func(a, b, c):
#     print('a = %s' %a)
#     print('b = %s' %b)
#     print('c = %s' %c)
#
#
# func(1, c=3)


# def howlong(first, *other):
#     return print(1 + len(other))
#
#
# howlong(123, 456, 789)

# var1 = 123


# def func():
#     global var1
#     var1 = 456
#     print(var1)


# func()
# print(var1)

# list1 = [1, 2, 3]
# it = iter(list1)
# print(next(it))
# print(next(it))
# print(next(it))

# for i in range(10, 20, 2):
#     print(i)

# def frange(star, stop, step):
#     x = star
#     while x < stop:
#         yield x
#         x += step


# for i in frange(10, 20, 0.5):
#     print(i)
#
# def true(): return True
#
#
# def add(x, y):
#     return x + y
#
#
# lambda x, y: x + y
#
# print(add(1, 2))

# map()
# filter()
# reduce()
# zip()
# import functools
#
# a = [1, 2, 3, 4, 5, 6]
# b = [11, 22, 33, 44, 55, 66]
# print(list(filter(lambda x: x > 3, a)))
# print(list(map(lambda x: x + 1, a)))
# print(list(map(lambda x, y: x + y, a, b)))
# print(functools.reduce(lambda x, y: x + y, [2, 3, 4], 1))
#
# a = (1, 2, 3)
# b = (4, 5, 6)
# for i in zip(a, b):
#     print(i)

# dicta = {'a': 'aa', 'b': 'bb'}
# dictb = dict(zip(dicta.values(), dicta.keys()))
# print(dictb)

def func():
    a = 1
    b = 2
    return a + b


def sum(a):
    def add(b):
        return a + b

    return add


#  add 函数名称或函数的引用
#  add() 函数的调用


num1 = func()
num2 = sum(2)
# print(type(num1))
# print(type(num2))
print(num2)
print(num2(4))
