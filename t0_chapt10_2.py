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
