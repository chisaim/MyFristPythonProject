def print_me():
    print('me')


# print_me()

with open("name.txt") as f:
    for line in f:
        print(line)
