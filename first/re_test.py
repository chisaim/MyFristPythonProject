import re

# . ^ $ * + ? {m} {m,n} \ \d \D \s ()
# ^$
# .*?
# .匹配一个字符,包括字母和数字 ... abc或123
# ^以什么样的内容为开头 ^abc abced
# $以什么样的内容为结尾 $cde abcde
# *匹配前面的字符出现0次到多次

p = re.compile('jpg$')
print(p.match('foobar.jpg'))
print(p.search())
