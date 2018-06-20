#  记录星座
zodiac_name = ("白羊座", "金牛座", "双子座", "巨蟹座", "狮子座", "处女座",
               "天秤座", "天蝎座", "射手座", "摩羯座", "水瓶座", "双鱼座")
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
               (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

# (month, day) = (2, 15)
# zodiac_day = filter(lambda x: x <= (month, day), zodiac_days)
# zodiac_len = len(list(zodiac_day)) % 12
# print(zodiac_name[zodiac_len])

int_month = int(input("请输入月份"))
int_day = int(input("请输入日期"))
for zd_num in range(len(zodiac_days)):
    if zodiac_days[zd_num] >= (int_month, int_day):
        print(zodiac_name[zd_num])
        break
    elif int_month == 12 and int_day > 23:
        print(zodiac_name[0])
        break
