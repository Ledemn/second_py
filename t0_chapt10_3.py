print('\n', '#001: aggregation', '-' * 38)  # --------------------------------


class Bill:
    def __init__(self, description):
        self.description = description


class Tail:
    def __init__(self, length):
        self.length = length


class Duck:
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail

    def about(self):
        print('This duck has a', self.bill.description, 'bill and a',
              self.tail.length, 'tail.')


a_tail = Tail('long')
a_bill = Bill('wide orange')
duck = Duck(a_bill, a_tail)

print(duck.about())


#
#
#
print('\n\n\n', '#002: namedtuple', '-' * 38)  # ------------------------------

from collections import namedtuple
Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')

print(duck)
print(duck.bill)
print(duck.tail)


print('\n')  # ----------------------------------
parts = {'bill': 'wide orange', 'tail': 'long'}
duck2 = Duck(**parts)           # >>> duck2 = Duck(bill = 'wide orange', tail = 'long')
print(duck2)


print('\n')  # ----------------------------------
duck3 = duck2._replace(tail='magnificent', bill='crushing')
print(duck2)
print(duck3)


print('\n')  # ----------------------------------
duck_dict = {'bill': 'wide orange', 'tail': 'long'}
print(duck_dict)


print('\n')  # ----------------------------------
duck_dict['color'] = 'green'
print(duck_dict)


print('\n')  # --- but not into namedtuple -------------------------
# duck.color = 'green'    # AttributeError: 'Duck' object has no attribute 'color'


#
#
#
print('\n\n\n', '#003: dataclasses (in v3.7+)', '-' * 26)  # -----------------------------


class TeenyClass:
    def __init__(self, name):
        self.name = name


teeny = TeenyClass('itsy')
print(teeny.name)


# ----------------------------------


from dataclasses import dataclass


@dataclass
class TeenyDataClass:
    name: str


teeny = TeenyDataClass('bitsy')
print(teeny.name)


# ----------------------------------
from dataclasses import dataclass


@dataclass
class AnimalClass:
    name: str
    habitat: str
    teeth: int = 0


snowman = AnimalClass('yeti', 'Himalayas', 46)
print(snowman)
duck = AnimalClass('duck', 'lake')
print(duck)

print(duck.habitat)
print(snowman.teeth)
