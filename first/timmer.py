import time

import model_test as model


# starttime = time.time()

# time.sleep(3)

# endtime = time.time()

# print(endtime - starttime)


# def timmer(func):
#     def nei():
#         start_time = time.time()
#         func()
#         end_time = time.time()
#         print("运行时间 %s 秒" % (end_time - start_time))
#     return nei


# @timmer
# def i_can_sleep():
#     time.sleep(3)


# i_can_sleep()

def new_tip(args):
    def tip(func):
        def nei(a, b):
            print("start %s %s" % (args, func.__name__))
            func(a, b)
            print("stop")

        return nei

    return tip


@new_tip('tip_add')
def add(a, b):
    print(a + b)


@new_tip('tip_sub')
def sub(a, b):
    print(a - b)


# add(4, 5)
# sub(4, 5)

model.print_me()
