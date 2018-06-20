#
# year = int(input("请输入:"))

# try:
#     year = int(input("请输入:"))
# except ValueError:
#     print("年份请输入数字")
# finally:
#     print("close")

# try:
#     a=123
#     a.append()
# except AttributeError:
#     print("该对象没有这个属性，请选择正确的对象")
# finally:
#     print("close")

# except (ValueError, AttributeError, KeyError)

# try:
#     print(1/0)
# except ZeroDivisionError as e:
#     print("0不能做除数 %s" %e)
# finally:
#     print("close")

# try:
#     raise NameError("helloError")
# except NameError:
#     print("my custom error")

try:
    a = open("name1.txt")
except Exception as e:
    print(e)
finally:
    a.close()
