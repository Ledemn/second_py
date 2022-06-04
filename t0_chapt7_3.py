# chapt7_day3
#

print('\n', '#034_a', '-' * 50)
# 34a-----------------------------------------------for in
cheeses = ['brie', 'gjetost', 'havarti']
print(cheeses)
for cheese in cheeses:
    print(cheese)


print('\n\n', '#034_b', '-' * 30)
# 34b-----------------------------------------------
# cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    if cheese.startswith('g'):
        print("I won't eat anything that starts with 'g'")
        break
    else:
        print(cheese)


print('\n\n', '#034_c', '-' * 30)
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


print('\n\n', '#034_d', '-' * 30)
# 34d-----------------------------------------------
cheeses = []
for cheese in cheeses:
    print('This shop has some lovely', cheese)
    break
else:   # no break means no cheese
    print('This is not much of a cheese shop, is it?')


print('\n\n', '#034_f', '-' * 30)
# 34f-----------------------------------------------
cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    print('This shop has some lovely', cheese)
    break
else:   # no break means no cheese
    print('This is not much of a cheese shop, is it?')


print('\n\n', '#034_g', '-' * 30)
# 34g-----------------------------------------------
for cheese in cheeses:
    print('This shop has some lovely', cheese, cheese)
    break
else:   # no break means no cheese
    print('This is not much of a cheese shop, is it?')


#
print('\n\n\n', '#037_a', '-' * 50)
# 37a-----------------------------------------------zip()
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "eat", fruit, "enjoy", dessert)


print('\n\n', '#037_b', '-' * 30)
# 37b-----------------------------------------------zip() dict
english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'
print(list(zip(english, french)))
print(dict(zip(english, french)))


print('\n\n', '#036', '-' * 50)
# 36------------------------------------------------


print('\n\n', '#037', '-' * 50)
# 37------------------------------------------------


print('\n\n', '#038', '-' * 50)
# 38------------------------------------------------


print('\n\n', '#036', '-' * 50)
# 36------------------------------------------------


print('\n\n', '#037', '-' * 50)
# 37------------------------------------------------


print('\n\n', '#038', '-' * 50)
# 38------------------------------------------------
