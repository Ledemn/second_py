# Chapt9. Day1

print('\n', '#001 DEF PASS', '-' * 42)  # -----------------------------------------


def do_nothing():
    pass


print(do_nothing())


print('\n\n', '#002 DEF', '-' * 47)  # --------------------------------------------


def make_a_sound():
    print('quack')


print(make_a_sound())


print('\n\n', '#003 DEF', '-' * 47)  # --------------------------------------------


def agree():
    return True


print(agree())


print('\n\n', '#004 if-else', '-' * 43)  # ----------------------------------------
if agree():
    print('Splendid!')
else:
    print('That was unexpected.')


print('\n\n', '#005 DEF', '-' * 47)  # --------------------------------------------


def echo(anything):
    return anything + ' ' + anything


print('\n\n', '#006 DEF', '-' * 47)  # --------------------------------------------
print(echo('Rumplestiltskin'))


print('\n\n', '#007 if-elif-else', '-' * 38)  # -----------------------------------


def commentary(color):
    if color == 'red':
        return "It's a tomato."
    elif color == 'green':
        return "It's a green pepper."
    elif color == 'bee purple':
        return "I don't know what it is, but only bees can see it."
    else:
        return "I've never heard of the color " + color + "."


comment = commentary('blue')
print(comment)


print('\n\n', '#008 None', '-' * 46)  # like False but not BOOL--------------------
thing = None
if thing:
    print("It's some thing")
else:
    print("It's no thing")


print('\n\n', '#009 IS', '-' * 48)  # ---------------------------------------------
thing = None
if thing is None:
    print("It's nothing")
else:
    print("It's some thing")


print('\n\n', '#010 (None, True, False)', '-' * 31)  # ---------------------------


def whatis(thing):
    if thing is None:
        print(thing, "is None")
    elif thing:
        print(thing, "is True")
    else:
        print(thing, "is False")


print(whatis(None))
print(whatis(True))
print(whatis(False))


print('\n\n', '#011 DEF', '-' * 47)  # -------------------------------------------
print(whatis(0))
print(whatis(0.0))
print(whatis(''))
print(whatis(""))
print(whatis(''''''))
print(whatis(()))
print(whatis([]))
print(whatis({}))
print(whatis(set()))

print(whatis(0.00001))
print(whatis([0]))
print(whatis(['']))
print(whatis(' '))


print('\n\n\n', '#012 DEF', '-' * 47)  # -----------------------------------------


def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}


print(menu('chardonnay', 'chicken', 'cake'))


print('\n\n', '#013 DEF: wrong positional/order', '-' * 23)  # -------------------
print(menu('beef', 'bagel', 'bordeaux'))


print('\n\n', '#014 DEF: arguments - keywords', '-' * 25)  # ----------------------
print(menu(entree='beef', dessert='bagel', wine='bordeaux'))


print('\n\n', '#015 DEF: mixed', '-' * 40)  # -------------------------------------
print(menu('frontenac', dessert='flan', entree='fish'))  # positional args are first


print('\n\n', '#016 DEF: parameters by default', '-' * 24)  # ---------------------


def menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}


print(menu('chardonnay', 'chicken'))


print('\n\n', '#017 DEF: default parameter is replaced by defined arg', '-')  # ---
# def menu(wine, entree, dessert='pudding'):
#    return {'wine': wine, 'entree': entree, 'dessert': dessert}
#

print(menu('dunkelfelder', 'duck', 'doughnut'))


print('\n\n', '#018 DEF: buggy', '-' * 40)  # --------------------------------------


def buggy(arg, result=[]):  # empty list at first call
    result.append(arg)
    print(result)


print(buggy('a'))
print(buggy('b'))
print(buggy('c'))


print('\n\n', '#019 DEF: works', '-' * 40)  # -------------------------------------


def works(arg):
    result = []
    result.append(arg)
    return result


print(works('a'))
print(works('b'))
print(works('c'))


print('\n\n', '#020 DEF: nonbuggy', '-' * 37)  # ----------------------------------


def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)


print(nonbuggy('a'))
print(nonbuggy('b'))
print(nonbuggy('c'))


print('\n\n', '#021 DEF: *', '-' * 44)  # ------------------------------------------


def print_args(*args):
    print('Positional argument tuple:', args)


print(print_args())
print(print_args(3, 2, 1, 'wait!', 'uh...'))


print('\n\n', '#022 DEF: required args + *', '-' * 28)  # --------------------------


def print_more(required1, required2, *args):
    print('Need this one:', required1)
    print('Need this one too:', required2)
    print('All the rest:', args)


print(print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax'))


print('\n\n', '#023 DEF: **', '-' * 43)  # dict--------------------------------


def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)


print(print_kwargs())
print(print_kwargs(wine='merlot', entree='mutton', dessert='macaroon'))


print('\n\n', '#024 DEF', '-' * 47)  # ----------------------------------------


def print_data(data, *, start=0, end=100):
    for value in (data[start:end]):
        print(value)


data = ['a', 'b', 'c', 'd', 'e', 'f']
print(print_data(data))
print(print_data(data, start=4))
print(print_data(data, end=2))


print('\n\n', '#025 DEF: changeable arguments', '-' * 25)  # --------------------
outside = ['one', 'fine', 'day']


def mangle(arg):
    arg[1] = 'terrible!'


print(outside)
print(mangle(outside))
print(outside)


print('\n\n', '#026 DEF: documentation help()', '-' * 25)  # -------------------


def echo(anything):
    'echo returns its input argument'
    return anything


# def print_if_true(thing, check):
#    '''
#    Prints the first argument if a second argument is true.
#    The operation is:
#        1. Check whether the *second* argument is true.
#        2. If it is, print the *first* argument.
#    '''
# if check:
#    print(thing)


print('\n\n', '#000 DEF', '-' * 47)  # ----------------------------------------
