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


print('\n\n', '#0xx ', '-' * 50)
# -----------------------------------------------


print('\n\n', '#0xx ', '-' * 50)
# -----------------------------------------------


print('\n\n', '#0xx ', '-' * 50)
# -----------------------------------------------
