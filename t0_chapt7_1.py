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



print('\n', '#027', '-' * 50)
# 27------------------------------------------------



print('\n', '#028', '-' * 50)
# 28------------------------------------------------
