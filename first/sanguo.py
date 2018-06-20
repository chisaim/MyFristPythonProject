#  读取人物名称
# f = open("name.txt", 'r', encoding='utf-8')
# data = f.read()
# print(data.split('|'))

#  读取兵器的名称
# f2 = open("weapon.txt", 'r', encoding='utf-8')
# data2 = f2.read()
# i = 1
# for line in f2.readlines():
#     if i % 2 == 1:
#         print(line.strip('\n'))
#     i += 1

#  读取三国原文
# f3 = open('sanguo.txt', 'r', encoding='utf-8')
# print(f3.read().replace('\n', ''))


def func(filename):
    print(open(filename, 'r', encoding='utf-8').read())
    print('test func')


func('name.txt')
