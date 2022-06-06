# chapt8_day1
#
print('\n', '#001', '-' * 50)
# 001-----------------------------------------------
empty_dict = {}
print(empty_dict)


print('\n\n', '#002', '-' * 50)
# 002-----------------------------------------------
bierce = {
    "day": "A period of twenty-four hours, mostly misspent",
    "positive": "Mistaken at the top of one's voice",
    "misfortune": "The kind of fortune that never misses",
}
print(bierce)


print('\n\n', '#003 (traditional way of creatind)', '-' * 20)
# 003-----------------------------------------------
acme_customer = {'first': 'Wile', 'middle': 'E', 'last': 'Coyote'}
print(acme_customer)


print('\n\n', '#004 using DICT()', '-' * 37)
# 004-----------------------------------------------
acme_customer = dict(first="Wile", middle="E", last="Coyote")
print(acme_customer)


print('\n\n', '#005', '-' * 50)
# 005-----------------------------------------------
lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
print(dict(lol))

# ----
lot = [('a', 'b'), ('c', 'd'), ('e', 'f')]
print(dict(lot))

# ----
tol = (['a', 'b'], ['c', 'd'], ['e', 'f'])
print(dict(tol))

# ----
los = ['ab', 'cd', 'ef']
print(dict(los))

# ----
tos = ('ab', 'cd', 'ef')
print(dict(tos))


print('\n\n', '#006', '-' * 50)
# 006-----------------------------------------------
pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
}
print(pythons)

pythons["Gilliam"] = "Gerry"
print(pythons)
pythons["Gilliam"] = "Terry"
print(pythons)


print('\n\n', '#007', '-' * 50)
# 007-----------------------------------------------
print(pythons['Chapman'])

# 007---
print('Groucho' in pythons)


print('\n\n', '#007 using GET()', '-' * 38)
# 007-----------------------------------------------
print(pythons.get('John'))
print(pythons.get('Cleese'))


print('\n\n', '#008 getting .KEYS()', '-' * 34)
# 008-----------------------------------------------
signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
print(signals)
print(signals.keys())
print(list(signals.keys()))


print('\n\n', '#009 .VALUES()', '-' * 40)
# 009-----------------------------------------------
print(signals.values())
print(list(signals.values()))


print('\n\n', '#010 .ITEMS()    LEN()', '-' * 32)
# 010-----------------------------------------------
print(signals.items())
print(list(signals.items()))
print(len(signals))


print('\n\n', '#011 {**a, **b}', '-' * 39)
# 011-----------------------------------------------
first = {'a': 'agony', 'b': 'bliss'}
second = {'b': 'bagels', 'c': 'candy'}
print({**first, **second})
third = {'d': 'donuts'}
print({**first, **third, **second})


print('\n\n', '#012 UPDATE()', '-' * 41)
# 012-----------------------------------------------
print(len(pythons))
others = {'Marx': 'Groucho', 'Howard': 'Moe'}
print(others)

pythons.update(others)
print(len(pythons))

print('\n')

first = {'a': 1, 'b': 2}
second = {'b': 'platypus'}
first.update(second)
print(first)


print('\n\n', '#013 DEL', '-' * 46)
# 013-----------------------------------------------
print(len(pythons))
del pythons['Marx']
del pythons['Howard']
print(pythons)
print(len(pythons))


print('\n\n', '#013 .POP() | GET() and DEL', '-' * 27)
# 013-----------------------------------------------
print(pythons.pop('Palin'))
print(len(pythons))
# re:   print(pythons.pop('Palin'))     # KeyError: 'Palin'
# -------
print(pythons.pop('First', 'Hugo'))     # with 2nd argument there are no changes
print(len(pythons))


print('\n\n', '#014 .CLEAR | = {}', '-' * 36)
# 014-----------------------------------------------
print(len(pythons))
pythons.clear()     # or pythons = {}
print(len(pythons))
print(pythons)


print('\n\n', '#015 IN', '-' * 47)
# 015-----------------------------------------------
pythons = {
    'Chapman': 'Graham', 'Cleese': 'John',
    'Jones': 'Terry', 'Palin': 'Michael', 'Idle': 'Eric'}
print(pythons)
print('Chapman' in pythons)
print('Palin' in pythons)
print('Gilliam' in pythons)


print('\n\n', '#016 =', '-' * 48)
# 016-----------------------------------------------
# signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
print(len(signals))
print(signals)
save_signals = signals
signals['blue'] = 'confuse everyone'
print(len(save_signals))
print(save_signals)


print('\n\n', '#017 .COPY()', '-' * 42)
# 017-----------------------------------------------
signals = {'green': 'go',
           'yellow': 'go faster',
           'red': 'smile for the camera'}

original_signals = signals.copy()       # copying before doing changes
signals['blue'] = 'confuse everyone'

print(len(signals))
print(len(original_signals))


print('\n\n', '#018 DEEPCOPY()', '-' * 39)
# 018-----------------------------------------------
signals = {'green': 'go',
           'yellow': 'go faster',
           'red': ['stop', 'smile']}

signals_copy = signals.copy()

print(signals)
print(signals_copy)

print(signals.keys())       # just 4or practice
print(signals['green'])     # just 4or practice
print(signals['red'])       # just 4or practice

signals['red'][1] = 'sweat'

print(signals)
print(signals_copy)
