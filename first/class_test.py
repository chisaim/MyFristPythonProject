# user1 = {'name': 'tom', 'hp': 100}
# user2 = {'name': 'jerry', 'hp': 80}


# def print_role(rolename):
#     print('name is %s , hp is %s ' % (rolename['name'], rolename['hp']))


# print_role(user1)
# print_role(user2)


class Player():
    def __init__(self, name, hp, occu):
        self.name = name
        self.hp = hp
        self.occu = occu

    def print_role(self):
        print('name is %s , hp is %s , occu is %s ' % (self.name, self.hp, self.occu))

    def update_name(self, new_name):
        self.name = new_name


class Animals():
    def __init__(self, hp=100):
        self.hp = hp

    def who_am_i(self):
        print("Animals's who am i")


class Monster(Animals):
    def __init__(self, hp=20):
        super().__init__(hp)

    def who_am_i(self):
        print("Monster's who am i")


class Boss(Animals):
    pass


user1 = Player('tom', 100, 'war')
user2 = Player('jerry', 80, 'master')
user1.print_role()
user2.print_role()

a1 = Monster()
a1.who_am_i()
print(isinstance(a1, Animals))
