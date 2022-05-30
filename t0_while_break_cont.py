guess_me = 7
number = 1

while True:
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
        break
    if number > guess_me:
        print("oops")
        break
    else:
        print(number + 1)
        break
