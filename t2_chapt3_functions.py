def do_twice(f):  # 1----------
    f()
    f()


def print_spam():
    print('SPAM')


do_twice(print_spam)

print('-' * 60)

# 2-----------------------------------------------------------

# def do_twice(f, a):       !!!
#    f()
#    a = len()              !!!


# def print_spam():
#    print('SPAM')


do_twice(print_spam)

print('-' * 60)


# 3-----------------------------------------------------------
def print_twice(arg):
    print("""
    A named sequence of instructions
    that performs some useful computation.
    Functions do not necessarily take arguments
    and return values.""")
    print(arg)
    print(arg)


print_twice()

print('-' * 60)


# 4-----------------------------------------------------------

def do_twice(func, arg):
    func(arg)
    func(arg)


do_twice(print_twice)

print('-' * 60)


# 5-----------------------------------------------------------

def do_four(func, arg):
    do_twice(func, arg)
    do_twice(func, arg)


do_twice(print, 'spam')
print('')

do_four(print, 'spam')
