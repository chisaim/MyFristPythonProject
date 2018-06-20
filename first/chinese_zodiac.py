#  记录生肖，根据年份来判断生肖
chinese_zodiac = "子丑寅卯辰巳午未申酉戌亥"
#  print(chinese_zodiac[0:4])
#  print(chinese_zodiac[-1])

year = 2018
print(year % 12)
print(chinese_zodiac[year % 12])
