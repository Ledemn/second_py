# Chapt8. Day4

print('\n\n', '#023 SET()', '-' * 45)
# -----------------------------------------------
empty_set = set()
print(empty_set)

even_numbers = {0, 2, 4, 6, 8}
print(even_numbers)
odd_numbers = {1, 3, 5, 7, 9}
print(odd_numbers)

print('---')
print(set('letters'))
print(set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon']))  # list to set
print(set(('Ummagumma', 'Echoes', 'Atom Heart Mother')))    # tuple to set
print(set({'apple': 'red', 'orange': 'orange', 'cherry': 'red'}))   # dic to set
reinder = set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'])
print(reinder)
print(len(reinder))


print('\n\n', '#024 .ADD()', '-' * 44)
# -----------------------------------------------
s = set((1, 2, 3))
print(s)
s.add(4)
print(s)


print('\n\n', '#025 .REMOVE()', '-' * 41)
# -----------------------------------------------
s = set((1, 2, 3))
print(s)
s.remove(3)
print(s)


print('\n\n', '#026 FOR IN', '-' * 44)
# -----------------------------------------------
furniture = set(('sofa', 'ottoman', 'table'))
print(furniture)
for piece in furniture:
    print(piece)


print('\n\n', '#027 IN', '-' * 48)
# -----------------------------------------------
drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}
print(drinks, '\n')

for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)

print('---')
for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
        print(name)


print('\n\n', '#028 operator &', '-' * 40)
# -----------------------------------------------
for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        print(name)

print('---')
for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
        print(name)

print('\n')
bruss = drinks['black russian']
wruss = drinks['white russian']

# print('---')
a = {1, 2}
b = {2, 3}
print(a)
print(b)


print(a & b)    # &
print('--- intersection()')
print(a.intersection(b))

print('\n')
print(bruss)
print(wruss)
print(bruss & wruss)    # &


print('\n\n\n', '#029 "|" or UNION()', '-' * 38)
# -----------------------------------------------
print(a | b)
print(a.union(b))
print('---')

print(bruss | wruss)


print('\n\n', '#030 "-" or .DIFFERENCE()', '-' * 37)
# -----------------------------------------------
print(a - b)
print(b - a)
print(a.difference(b))

print(bruss - wruss)
print(wruss - bruss)


print('\n\n', '#031 "^" or .symmetric_difference()', '-' * 20)
# -----------------------------------------------
print(a)
print(b)
print(a ^ b)
print(a.symmetric_difference(b))
print('---')

print(bruss)
print(wruss)
print(bruss ^ wruss)


print('\n\n', '#032 "<=" or .issubset()', '-' * 31)
# -----------------------------------------------
print(a <= b)
print(a.issubset(b))
print('---')

print(bruss)
print(wruss)
print(bruss <= wruss)   # wruss is subset of bruss
print(wruss <= bruss)
print('---')

print(a <= a)
print(a.issubset(a))

print('--- < ---')
print(a < b)
print(a < a)
print(bruss < wruss)


print('\n\n', '#033 ">=" or .issuperset()', '-' * 29)
# -----------------------------------------------
print(a)
print(b)
print(a >= b)
print(a.issuperset(b))
print('---')

print(bruss >= wruss)
print(wruss >= bruss)
print('---')

print(a >= a)
print(a.issuperset(a))

print('--- > ---')
print(a > b)
print(a > a)
print(wruss > bruss)


print('\n\n', '#033 ', '-' * 50)
# -----------------------------------------------
a_set = {number for number in range(1, 6) if number % 3 == 1}
print(a_set)


print('\n\n', '#034 FROZENSET()', '-' * 39)
# -----------------------------------------------
print(frozenset([3, 2, 1]))
print(frozenset([2, 1, 3]))
print(frozenset({3, 1, 2}))
print(frozenset((2, 3, 1)))
print('---')

fs = frozenset([3, 2, 1])
print(fs)
# fs.add(4)     # AttributeError: 'frozenset' object has no attribute 'add'


print('\n\n\n\n', '#035 REVISE-1', '-' * 50)
# -----------------------------------------------
marx_list = ['Groucho', 'Chico', 'Harpo']
print(marx_list)
marx_tuple = 'Groucho', 'Chico', 'Harpo'
print(marx_tuple)
marx_dict = {'Groucho': 'banjo', 'Chico': 'piano', 'Harpo': 'harp'}
print(marx_dict)
marx_set = {'Groucho', 'Chico', 'Harpo'}
print(marx_set)

print('---')

print(marx_list[2])
print(marx_tuple[2])
print(marx_dict['Harpo'])

print('Harpo' in marx_list)
print('Harpo' in marx_tuple)
print('Harpo' in marx_dict)
print('Harpo' in marx_set)


print('\n\n', '#036 REVISE-2', '-' * 42)
# -----------------------------------------------
marxes = ['Groucho', 'Chico', 'Harpo']
pythons = ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin']
stooges = ['Moe', 'Curly', 'Larry']

print(marxes)
print(pythons)
print(stooges)
print('---tuple_of_lists:')

tuple_of_lists = marxes, pythons, stooges
print(tuple_of_lists)
print('\n')


list_of_lists = [marxes, pythons, stooges]
print('---list_of_lists:')
print(list_of_lists)
print(print(list_of_lists[0][1]))
print('\n')


dict_of_lists = {'Marxes': marxes, 'Pythons': pythons, 'Stooges': stooges}
print('---dict_of_lists:')
print(dict_of_lists)


print('\n\n\n', '#EXERCISES 8.1')
# -----------------------------------------------



print('\n\n\n', '#EXERCISES 8.2')
# -----------------------------------------------



print('\n\n\n', '#EXERCISES 8.3')
# -----------------------------------------------



print('\n\n\n', '#EXERCISES 8.4')
# -----------------------------------------------



print('\n\n\n', '#EXERCISES 8.5')
# -----------------------------------------------



print('\n\n\n', '#EXERCISES 8.6')
# -----------------------------------------------

