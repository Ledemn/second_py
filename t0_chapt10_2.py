# Chapt10: Day2

print('\n', '#001 Adding a method', '-' * 35)  # --------------------------


class Car():
    def exclaim(self):
        print("I'm a Car!")


class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")

    def need_a_push(self):
        print("A little help here?")


give_me_a_car = Car()
give_me_a_yugo = Yugo()

print(give_me_a_yugo.need_a_push())
# print(give_me_a_car.need_a_push())      # AttributeError: 'Car' object has no attribute 'need_a_push'


#
#
#
# -----------------------------------------------------------------------------------
print('\n\n', '#002 SUPER()', '-' * 43)  # -----------------------------------------


class Person:
    def __init__(self, name):
        self.name = name


class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email


bob = EmailPerson('Bob Frapples', 'bob@frapples.com')

print(bob.name)
print(bob.email)


#
#
#
# -----------------------------------------------------------------------------------
print('\n\n', '#003 CLASS: mro()', '-' * 38)  # -------------------------------------


class Animal:
    def says(self):
        return 'I speak!'


class Horse(Animal):
    def says(self):
        return 'Neigh!'


class Donkey(Animal):
    def says(self):
        return 'Hee-haw!'


class Mule(Donkey, Horse):
    pass


class Hinny(Horse, Donkey):
    pass


print(Mule.mro())
print(Hinny.mro())

mule = Mule()
hinny = Hinny()

print(mule.says())
print(hinny.says())


#
#
#
# -----------------------------------------------------------------------------------
print('\n\n', '#004 direct access', '-' * 37)  # --------------------------------------


class Duck:
    def __init__(self, input_name):
        self.name = input_name


fowl = Duck('Daffy')
print(fowl.name)

fowl.name = 'Daphne'
print(fowl.name)


#
#
#
# -----------------------------------------------------------------------------------
print('\n\n', '#005 get_ set_', '-' * 41)  # -----------------------------------------


class Duck:
    def __init__(self, input_name):
        self.hidden_name = input_name

    def get_name(self):
        print('inside the getter')
        return self.hidden_name

    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name


don = Duck('Donald')
print(don.get_name())

don.set_name('Donna')

print(don.get_name())


#
#
#
# -----------------------------------------------------------------------------------
print('\n\n', '#006 property', '-' * 42)  # -----------------------------------------


# Method 1:
class Duck:
    def __init__(self, input_name):
        self.hidden_name = input_name

    def get_name(self):
        print('inside the getter')
        return self.hidden_name

    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

    name = property(get_name, set_name)     # added


don = Duck('Donald')
print(don.name)

don.name = 'Donna'
print(don.name)


# Method 2 with decorators: ------------------
class Duck:
    def __init__(self, input_name):
        self.hidden_name = input_name

    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name

    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name


fowl = Duck('Howard')
print(fowl.name)

fowl.name = 'Donald'
print(fowl.name)


#
#
#
# -----------------------------------------------------------------------------------
print('\n\n\n', '#007 ', '-' * 50)  # -----------------------------------------


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius


c = Circle(5)
print(c.radius)
print(c.diameter)

c.radius = 7
print(c.radius)
print(c.diameter)

# c.diameter = 20   # AttributeError: can't set attribute 'diameter'


#
#
#
# -----------------------------------------------------------------------------------
print('\n\n', '#008 ', '-' * 50)  # -----------------------------------------


class Duck:
    def __init__(self, input_name):
        self.__name = input_name

    @property
    def name(self):
        print('inside the getter')
        return self.__name

    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name


fowl = Duck('Howard')
print(fowl.name)

fowl.name = 'Donald'
print(fowl.name)
# print(fowl.__name)        # AttributeError: 'Duck' object has no attribute '__name'.
print(fowl._Duck__name)     # optional knowledge


#
#
#
# -----------------------------------------------------------------------------------
print('\n\n', '#009 ', '-' * 50)  # -----------------------------------------


class Fruit:
    color = 'red'


blueberry = Fruit()
print(Fruit.color)              # red
print(blueberry.color)          # red
# print(Fruit.mro())

blueberry.color = 'blue'
print(blueberry.color)          # blue
print(Fruit.color)              # red


Fruit.color = 'orange'
print(Fruit.color)              # orange
print(blueberry.color)          # blue

# ! But it will affect new ones:
new_fruit = Fruit()
print(new_fruit.color)          # orange


#
#
#
# -----------------------------------------------------------------------------------
print('\n\n', '#010 @classmethod', '-' * 38)  # --------------------------------


class A:
    count = 0

    def __init__(self):
        A.count += 1

    def exclaim(self):
        print("I'm an A!")

    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.")


easy_a = A()
breezy_a = A()
wheezy_a = A()

print(A.kids())


#
#
#
# -----------------------------------------------------------------------------------
print('\n\n', '#011 @staticmethod', '-' * 37)  # ------------------------------------


class CoyoteWeapon:
    @staticmethod
    def commercial():
        print('This CoyoteWeapon has been brought to you by Acme')


print(CoyoteWeapon.commercial())


#
#
#
# -----------------------------------------------------------------------------------
print('\n\n', '#012 ', '-' * 50)  # -----------------------------------------


class Quote:
    def __init__(self, person, words):
        self.person = person
        self.words = words

    def who(self):
        return self.person

    def says(self):
        return self.words + '.'


class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'


class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'


# Let's make few objects:
# 1:
hunter = Quote('Elmer Fudd', "I'm hunting wabbits")     # __init__(self, person, words):
#
print(hunter.who())             # test1
print(hunter.who(), 'says:')    # test2
print(hunter.who(), 'says:', hunter.says())


# 2:
hunted1 = QuestionQuote('Bugs Bunny', "What's up, doc")
#
print(hunted1.who(), 'says:', hunted1.says())


# 3:
hunted2 = ExclamationQuote('Daffy Duck', "It's rabbit season")
#
print(hunted2.who(), 'says:', hunted2.says())


print('\n', '#012-p2 ', '-' * 20)  # -----------------------------------------




#
#
#
# -----------------------------------------------------------------------------------
print('\n\n', '#000 ', '-' * 50)  # -----------------------------------------

#
#
#
# -----------------------------------------------------------------------------------
print('\n\n', '#000 ', '-' * 50)  # -----------------------------------------


#
#
#
# -----------------------------------------------------------------------------------
print('\n\n', '#000 ', '-' * 50)  # -----------------------------------------
