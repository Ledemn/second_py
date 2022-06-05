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


print('\n\n', '#012', '-' * 50)
# 012-----------------------------------------------


print('\n\n', '#012', '-' * 50)
# 012-----------------------------------------------


print('\n\n', '#012', '-' * 50)
# 012-----------------------------------------------


print('\n\n', '#012', '-' * 50)
# 012-----------------------------------------------
