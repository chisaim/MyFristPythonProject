import time

print(time.time())
print(time.localtime())
print(time.strftime('%Y-%m-%d %H:%M:%S'))

import datetime

print(datetime.datetime.now())
start_time = datetime.timedelta(minutes=10)
print(datetime.datetime.now() + start_time)

one_day = datetime.datetime(2008, 5, 20)
new_day = datetime.timedelta(days=10)
print(one_day + new_day)

import random

print(random.randint(1, 5))
print(random.choice(['aa', 'bb', 'cc']))
