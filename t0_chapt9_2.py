# Chapt9: Day5 (new file)
#
print('\n', '#028 DEF: INNER', '-' * 40)  # -----------------------------------


# 1:
def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)


print(outer(4, 7), '\n')  # 4 + 7 = 11


# 2:
def knights(saying):
    def inner(quote):   # adding text to arg
        return "We are the knights who say: '%s'" % quote
    return inner(saying)


print(knights('Ni!'), '\n')


# 3:
def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    return inner2


a = knights2('Duck')
b = knights2('Hasenpfeffer')
print(type(a))
print(a)
print(type(b))
print(b)

print(a())
print(b())


print('\n\n\n', '#029 DEF: + lambda', '-' * 37)  # -----------------------------


# 1:
def edit_story(words, func):
    for word in words:
        print(func(word))


# 2:
stairs = ['thud', 'meow', 'thud', 'hiss']


# 3:
def enliven(word):
    return word.capitalize() + '!'


# 4:
print(edit_story(stairs, enliven))

# 4.1:
print('\n')
print(edit_story(stairs, lambda word: word.capitalize() + '!'))


print('\n\n\n', '#030 DEF: GENERATORS', '-' * 35)  # ------------------------
# 1:
print(sum(range(1, 101)), '\n')


# 2:
def my_range(first=0, last=100, step=1):
    number = first
    while number < last:
        yield number
        number += step


print(my_range)

ranger = my_range(1, 5)

for x in ranger:
    print(x)

print(ranger)

for try_again in ranger:    # this time the generator is empty.
    print(try_again)


print('\n\n\n', '#031 DEF: DECORATORS', '-' * 35)  # --------------------------------


# 1:
def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result

    return new_function


# 2:
def add_ints(a, b):
    return a + b


print(add_ints(3, 5), '\n')


# 3:
cooler_add_ints = document_it(add_ints)     # creating manually
print(cooler_add_ints(3, 5))
print('\n')


# 3.1:                                      # alternative way
@document_it
def add_ints(a, b):
    return a + b


print(add_ints(3, 5))
print('\n')


# -----------------------------------more then ONE @:
def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function


@document_it    # runs 2nd
@square_it      # runs 1st (closest to function runs first)
def add_ints(a, b):
    return a + b


print(add_ints(3, 5))
print('\n')


# --------------------------let's try to change @@ order:
@square_it          # runs 2nd
@document_it        # runs 1st
def add_ints(a, b):
    return a + b


print(add_ints(3, 5))
print('\n')


print('\n\n\n', '#032 DEF: NAMES', '-' * 40)  # --------------------------------
animal = 'fruitbat'     # global variable


def print_global():
    print('inside print_global:', animal)


print('at the top level:', animal)
print(print_global())
print('\n')


# # # --------------------trying to get and then change the global variable 'animal':
def change_and_print_global():
    print('inside change_and_print_global:', animal)    # getting at first...
#    animal = 'wombat'                                  # and then changing!
    print('after the change:', animal)


print(change_and_print_global())
# >>> UnboundLocalError: local variable 'animal' referenced before assignment
# # # -------------------------------
print('\n')


def change_local():
    animal = 'wombat'
    print('inside change_local:', animal, id(animal))


print(change_local())
print(animal, id(animal))


print('\n\n\n', '#032 DEF: locals() globals()', '-' * 27)  # ------------------


# ------------------------------ver.local:
def change_and_print_global():
#   global animal
    animal = 'wombat'
    print('inside change_and_print_global:', animal)


print(animal)
print(change_and_print_global())
print(animal)


print('\n')


# ------------------------------ver.global:
def change_and_print_global():
    global animal
    animal = 'wombat'
    print('inside change_and_print_global:', animal)


print(animal)
print(change_and_print_global())
print(animal)


print('\n\n\n', '#000 DEF', '-' * 47)  # --------------------------------------


print('\n\n\n', '#000 DEF', '-' * 47)  # --------------------------------------


print('\n\n\n', '#000 DEF', '-' * 47)  # --------------------------------------


print('\n\n\n', '#000 DEF', '-' * 47)  # --------------------------------------

