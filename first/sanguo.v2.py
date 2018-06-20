import re_test


def find_item(hero):
    with open('sanguo.txt', 'r', encoding='utf-8') as f:
        data = f.read().replace('\n', '')
        name_num = re_test.findall(hero, data)
        print("主角 %s 出现次数 %s 次" % (hero, len(name_num)))
    return len(name_num)


#  读取人物名称
name_dic = {}
with open("name.txt", 'r', encoding='utf-8') as f:
    for line in f:
        names = line.split('|')
        for n in names:
            print(n)
            name_num = find_item(n)
            name_dic[n] = name_num
name_sorted = sorted(name_dic.items(), key=lambda item:item[1], reverse=True)
print(name_sorted[0:10])
