#
import time

# year = int(input("请输入:"))
chinese_zodiac = "子丑寅卯辰巳午未申酉戌亥"
# print(chinese_zodiac[year % 12])

for cz in chinese_zodiac:
    print(cz)
for i in range(1, 13):
    print(i)
for year in range(2000, 2019):
    print("%s 年的生肖是 %s" % (year, chinese_zodiac[year % 12]))
