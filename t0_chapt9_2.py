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


print('\n\n\n', '#031 DEF', '-' * 47)  # --------------------------------------


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


print('\n\n\n', '#000 DEF', '-' * 47)  # --------------------------------------


print('\n\n\n', '#000 DEF', '-' * 47)  # --------------------------------------


print('\n\n\n', '#000 DEF', '-' * 47)  # --------------------------------------


print('\n\n\n', '#000 DEF', '-' * 47)  # --------------------------------------

