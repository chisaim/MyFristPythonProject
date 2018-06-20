#

import time  # 导入时间模块

vec = [2, 4, 6]
print([[x, x ** 3] for x in vec if x > 3])

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print([[row[i] for row in matrix] for i in range(4)])

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
enum = enumerate(['gallahad', 'thepure', 'robin', 'thebrave'])
for k, v in enum:
    print(k, v)
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
    print('{0}:{1}'.format(q, a))
print(time.time())
