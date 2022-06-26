# Chapt10: Day1

print('\n', '#001 CLASS', '-' * 45)  # -----------------------------------------


class Cat:      # option Cat()
    pass        # empty class


a_cat = Cat()           # new object
another_cat = Cat()     # another new object

print(a_cat)
print(type(a_cat))
print(another_cat)
print(type(another_cat))


print('\n\n', '#002 ', '-' * 50)  # --------------------------------------------
a_cat.age = 3
a_cat.name = "Mr. Fuzzybuttons"
a_cat.nemesis = another_cat

print(a_cat.age)
print(a_cat.name)
print(a_cat.nemesis)
# print(a_cat.nemesis.name)       # AttributeError: 'Cat' object has no attribute 'name'

a_cat.nemesis.name = "Mr. Bigglesworth"
print(a_cat.nemesis.name)

print(another_cat.name)


print('\n\n', '#003 METHOD: __init__', '-' * 34)  # -------------------------


# 2:
class Cat:
    def __init__(self):
        pass


#
#
# 3:
class Cat():
    def __init__(self, name):
        self.name = name


furball = Cat('Grumpy')

print(type(furball))
print(furball)

print(type(furball.name))
print(furball.name)

print('Our latest addition: ', furball.name)


print('\n\n\n', '#004 ', '-' * 50)  # -----------------------------------------


class Car():
    pass


class Yugo(Car):
    pass


print(issubclass(Yugo, Car))    # checking

give_me_a_car = Car()
give_me_a_yugo = Yugo()


print('\n\n', '#005 ', '-' * 50)  # -----------------------------------------


class Car():
    def exclaim(self):
        print("I'm a Car!")


class Yugo(Car):
    pass


give_me_a_car = Car()
give_me_a_yugo = Yugo()

print(give_me_a_car.exclaim())
print(give_me_a_yugo.exclaim())


print('\n\n', '#006 ', '-' * 50)  # -----------------------------------------


class Car():
    def exclaim(self):
        print("I'm a Car!")


class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")


give_me_a_car = Car()
give_me_a_yugo = Yugo()

print(give_me_a_car.exclaim())
print(give_me_a_yugo.exclaim())


print('\n\n', '#007 ', '-' * 50)  # -----------------------------------------


class Person():
    def __init__(self, name):
        self.name = name


class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name


class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"


person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')

print(person.name)
print(doctor.name)
print(lawyer.name)
