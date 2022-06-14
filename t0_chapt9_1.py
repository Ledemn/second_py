# Chapt9. Day1

print('\n', '#001 DEF PASS', '-' * 42)  # -----------------------------------------------


def do_nothing():
    pass


print(do_nothing())


print('\n\n', '#002 DEF', '-' * 47)  # -----------------------------------------------


def make_a_sound():
    print('quack')


print(make_a_sound())


print('\n\n', '#003 DEF', '-' * 47)  # -----------------------------------------------


def agree():
    return True


print(agree())


print('\n\n', '#004 if-else', '-' * 43)  # -------------------------------------------
if agree():
    print('Splendid!')
else:
    print('That was unexpected.')


print('\n\n', '#005 DEF', '-' * 47)  # -----------------------------------------------


def echo(anything):
    return anything + ' ' + anything


print('\n\n', '#006 DEF', '-' * 47)  # -----------------------------------------------
print(echo('Rumplestiltskin'))


print('\n\n', '#007 if-elif-else', '-' * 38)  # -------------------------------------


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


print('\n\n', '#008 None', '-' * 46)  # like False but not BOOL-----------------------
thing = None
if thing:
    print("It's some thing")
else:
    print("It's no thing")


print('\n\n', '#009 IS', '-' * 48)  # -----------------------------------------------
thing = None
if thing is None:
    print("It's nothing")
else:
    print("It's some thing")


print('\n\n', '#010 (None, True, False)', '-' * 31)  # -----------------------------------------------


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


print('\n\n', '#011 DEF', '-' * 47)  # -----------------------------------------------
print(whatis(0))
print(whatis(0.0))
print(whatis(''))
print(whatis(""))
print(whatis(''''''))
print(whatis( () ))
print(whatis( [] ))
print(whatis( {} ))
print(whatis( set() ))

print(whatis(0.00001))
print(whatis( [0] ))
print(whatis( [''] ))
print(whatis(' '))


print('\n\n\n', '#000 DEF', '-' * 47)  # -----------------------------------------------


print('\n\n', '#000 DEF', '-' * 47)  # -----------------------------------------------


print('\n\n', '#000 DEF', '-' * 47)  # -----------------------------------------------


print('\n\n', '#000 DEF', '-' * 47)  # -----------------------------------------------
