# coding = utf-8
file1 = open("name.txt", "w")
file1.write("曹操")
file1.close()

# file2 = open("name.txt", 'r')
# print(file2.readline())
# file2.close()

file3 = open("name.txt", 'a')
file3.write("刘备")
file3.close()
# file2.seek(5, 0)
# file2.seek(5, 1)
# file2.seek(5, 2)
