import copy

print('\n', '#001', '-' * 50)
# 1-------------------------------------------------
one_marx = "Groucho", "Chico", "Harpo"
print(one_marx)


print('\n', '#002', '-' * 50)
# 2-------------------------------------------------
a, b, c = one_marx
print(a, b, c)

print(('Groucho',) + ('Chico', 'Harpo'))


print('\n', '#003', '-' * 50)
# 3-------------------------------------------------
words = ('fresh', 'out', 'of', 'ideas')
for word in words:
    print(word)


print('\n', '#004', '-' * 50)
# 4-------------------------------------------------
t1 = ("Fee", "Fie", "Foe")
t2 = ("Flop",)
t3 = ("Fyy",)
print(t1 + t2)

t1 += t2
print(t1)

t1 += t3
print(t1)


print('\n', '#005', '-' * 50)
# 5-------------------------------------------------
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print(weekdays)
print(type(weekdays))


print('\n', '#006', '-' * 50)
# 6-------------------------------------------------
print(list("halo002"))


print('\n', '#007', '-' * 50)
# 7-------------------------------------------------
a_tuple = ('ready', 'fire', 'aim')
print(list(a_tuple[1]))


print('\n', '#008', '-' * 50)
# 8-------------------------------------------------
talk_like_a_pirate_day = '9/19/2019'
print(talk_like_a_pirate_day)
print(talk_like_a_pirate_day.split("/"))


print('\n', '#009', '-' * 50)
# 9-------------------------------------------------
splitme = 'a/b//c/d///e'
print(splitme.split("/"))
print(splitme.split("//"))


print('\n', '#010', '-' * 50)
# 10------------------------------------------------
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes)
print(marxes[-3])
print(marxes[::-3])
print(marxes[::-1])


print('\n', '#011', '-' * 50)
# 11------------------------------------------------
marxes.reverse()
print(marxes)
marxes.reverse()
print(marxes)


print('\n', '#012', '-' * 50)
# 12------------------------------------------------
marxes.append('Zeppo')
print(marxes)
marxes.insert(1, 'Gummo')
print(marxes)


print('\n', '#013', '-' * 50)
# 13------------------------------------------------
print(["blah"] * 3)


print('\n', '#014', '-' * 50)
# 14------------------------------------------------
print(marxes)

others = ['Unno', 'Karl']
print(others)
marxes.extend(others)   # + or +=       marxes += others
print(marxes)


print('\n', '#015', '-' * 50)
# 15------------------------------------------------
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.append(others)
print(marxes)


print('\n', '#016', '-' * 50)
# 16------------------------------------------------
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes)
marxes[2] = 'Wanda'
print(marxes)


print('\n', '#017', '-' * 50)
# 17------------------------------------------------
numbers = [1, 2, 3, 4, 5, 6]
print(numbers)
numbers[1:2] = [10, 11]
print(numbers)


print('\n', '#018', '-' * 50)
# 18------------------------------------------------
numbers = [1, 2, 3, 4, 5, 6]
print(numbers)
numbers[1:3] = [7, 8, 9, 10]
print(numbers)


print('\n', '#019', '-' * 50)
# 19------------------------------------------------
numbers = [1, 2, 3, 4]
print(numbers)
numbers[1:3] = []
print(numbers)


print('\n', '#020', '-' * 50)
# 20------------------------------------------------
numbers = [1, 2, 3, 4, 5]
print(numbers)
numbers.insert(1, [10, 11, 12])
print(numbers)


print('\n', '#021', '-' * 50)
# 21a-----------------------------------------------
numbers = [1, 2, 3, 4]
print(numbers)
numbers[1:3] = (98, 99, 100)
print(numbers)

# 21b--
numbers = [1, 2, 3, 4]
print(numbers)
numbers[1:3] = 'wat?'
print(numbers)


print('\n', '#022', '-' * 50)
# 22------------------------------------------------
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Karl']
print(marxes)
print(marxes[-1])
del marxes[-1]
print(marxes)


print('\n', '#023', '-' * 50)
# 23------------------------------------------------
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo']
print(marxes)
del marxes[1]
print(marxes)


print('\n', '#024', '-' * 50)
# 24------------------------------------------------
print(marxes)
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.remove('Groucho')
print(marxes)


print('\n', '#025', '-' * 50)
# 25------------------------------------------------
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes)
print(marxes.pop())
print(marxes)
print(marxes.pop(1))
print(marxes)


print('\n', '#026', '-' * 50)
# 26------------------------------------------------
work_quotes = ['Working hard?', 'Quick question!', 'Number one priorities!']
print(work_quotes)
work_quotes.clear()
print(work_quotes)


print('\n', '#027', '-' * 50)
# 27a-----------------------------------------------
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes)
print(marxes.index('Chico'))

# 27b--
simpsons = ['Lisa', 'Bart', 'Marge', 'Homer', 'Bart']
print(simpsons)
print(simpsons.index('Bart'))   # first result only


print('\n', '#028', '-' * 50)
# 28a-----------------------------------------------
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print('Groucho' in marxes)
print('Bob' in marxes)

# 28b--
words = ['a', 'deer', 'a' 'female', 'deer']
print(words)
print('deer' in words)


print('\n', '#029', '-' * 50)
# 29a-----------------------------------------------
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes)
print(marxes.count('Harpo'))
print(marxes.count('Bob'))

# 29b--
snl_skit = ['cheeseburger', 'cheeseburger', 'cheeseburger']
print(snl_skit)
print(snl_skit.count('cheeseburger'))


print('\n', '#030', '-' * 50)
# 30a-----------------------------------------------
print(marxes)
print(type(marxes))
print(', '.join(marxes))
print(type(', '.join(marxes)))

print('\n')
# 30b--
friends = ['Harry', 'Hermione', 'Ron']
print(friends)
print(type(friends))
print(', '.join(friends))
print(type(', '.join(friends)))


print('\n')
separator = ' * '
joined = separator.join(friends)
print(joined)
print(type(joined))
separated = joined.split(separator)
print(separated)
print(type(separated))
print(f'Q: separated == friends?    A: {separated == friends}')


print('\n\n', '#031', '-' * 50)
# 31---------------------------------------sorted()
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes)
marxes.append('Karl')
marxes.append('Clark')
print(sorted(marxes))
print(marxes)
sorted_marxes = sorted(marxes)
print(sorted_marxes)
# -------------------------------sort()
marxes.sort()
print(marxes)
print(len(marxes))

# --------
numbers = [2, 1, 4.0, 3]
print(numbers)
numbers.sort()
print(numbers)


print('\n', '#032', '-' * 50)
# 32-----------------------------------=------------
a = [1, 2, 3]
print(a)
b = a
print(b)
a[0] = 'fooo'
print(a, b)
b[0] = 'winwin'
print(a, b)


print('\n\n', '#033', '-' * 50)
# 33---------------------------------copying-----------
a = [1, 2, 3]
b = a.copy()    # is a copy of 'a'
c = list(a)     # is a copy of 'a'
d = a[:]        # is a copy of 'a'
print(a, b, c, d)

a[0] = 'integer lists are boring'
print(a)
print(a, b, c, d)


print('\n')
# -------
a = [1, 2, [8, 9]]
print(f'list a = {a}')
print(f'list b = {b}')
print(f'list c = {c}')
print(f'list d = {d}')
b = a.copy()    # is a copy of 'a'
c = list(a)     # is a copy of 'a'
d = a[:]        # is a copy of 'a'
print(a, b, c, d)


print('\n')
print('\n', 'before deepcopy', '-' * 8)
# --------------deepcopy

a = [1, 2, [8, 9, 10]]
b = copy.deepcopy(a)    # is a deepcopy of 'a'
c = list(a)             # is a copy of 'a'
d = a[:]                # is a copy of 'a'
print(a)
print(b)
print(c)
print(d)
print('\n', 'after deepcopy', '-' * 8)
a[2][2] = 12
print(a)
print(b)
print(c)
print(d)


print('\n\n', '#034', '-' * 50)
# 34------------------------------------------------


print('\n', '#035', '-' * 50)
# 35------------------------------------------------


print('\n', '#036', '-' * 50)
# 36------------------------------------------------


print('\n', '#037', '-' * 50)
# 37------------------------------------------------


print('\n', '#038', '-' * 50)
# 38------------------------------------------------
