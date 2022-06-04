# chapt7_day3
#

print('\n', '#034_a', '-' * 50)
# 34a-----------------------------------------------for in
cheeses = ['brie', 'gjetost', 'havarti']
print(cheeses)
for cheese in cheeses:
    print(cheese)


print('\n', '#034_b', '-' * 30)
# 34b-----------------------------------------------
# cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    if cheese.startswith('g'):
        print("I won't eat anything that starts with 'g'")
        break
    else:
        print(cheese)


print('\n', '#034_c', '-' * 30)
# 34c-----------------------------------------------
# cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    if cheese.startswith('x'):
        print("I won't eat anything that starts with 'x'")
        break
    else:
        print(cheese)
else:
    print("Didn't find anything that started with 'x'")


print('\n', '#034_d', '-' * 30)
# 34d-----------------------------------------------
cheeses = []
for cheese in cheeses:
    print('This shop has some lovely', cheese)
    break
else:  # no break means no cheese
    print('This is not much of a cheese shop, is it?')


print('\n', '#034_f', '-' * 30)
# 34f-----------------------------------------------
cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    print('This shop has some lovely', cheese)
    break
else:  # no break means no cheese
    print('This is not much of a cheese shop, is it?')


print('\n', '#034_g', '-' * 30)
# 34g-----------------------------------------------
for cheese in cheeses:
    print('This shop has some lovely', cheese, cheese)
    break
else:  # no break means no cheese
    print('This is not much of a cheese shop, is it?')


#
print('\n\n\n', '#035_a', '-' * 50)
# 35a-----------------------------------------------zip()
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "eat", fruit, "enjoy", dessert)


print('\n', '#035_b', '-' * 30)
# 35 b-----------------------------------------------zip() dict
english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'
print(list(zip(english, french)))
print(dict(zip(english, french)))


print('\n\n\n', '#036v1', '-' * 50)
# 36 v1----------------------------------------------
number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)
print(number_list)


print('\n', '#036v2', '-' * 20)
# 36 v2----------------------------------------------
number_list = []
for number in range(1, 6):
    number_list.append(number)
print(number_list)


print('\n', '#036v3', '-' * 20)
# 36 v3----------------------------------------------
number_list = list(range(1, 6))
print(number_list)


print('\n\n\n', '#037 v-1/2/3/4', '-' * 44)
# 37 v1----------------------------------------------
number_list = [number for number in range(1, 6)]
print(number_list)


# 37 v2---
number_list = [number-1 for number in range(1, 6)]
print(number_list)

# 37 v3---
a_list = [number for number in range(1, 6) if number % 2 == 1]
print(a_list)

# 37 v4---
a_list = []
for number in range(1, 6):
    if number % 2 == 1:
        a_list.append(number)
print(a_list)


print('\n\n', '#038', '-' * 50)
# 38------------------------------------------------
rows = range(1, 4)
cols = range(1, 3)
for row in rows:
    for col in cols:
        print(row, col)

# -----------

rows = range(1, 4)
cols = range(1, 3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)

# -----------

for row, col in cells:
    print(row, col)


print('\n\n', '#039', '-' * 50)
# 39------------------------------------------------
small_birds = ['hummingbird', 'finch']
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
carol_birds = [3, 'French hens', 2, 'turtledoves']
all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]
print(all_birds)

# ---------
print('\n')
# ---------TEST
for brd in all_birds:
    print(brd)
# ---------21
print('\n', '-' * 21)

print(all_birds[0])
print(all_birds[1])
print(all_birds[1][0])
