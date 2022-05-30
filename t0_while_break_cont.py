guess_me = 5
number = 1

# while True:
#    if number < guess_me:
#        print("too low")
#    elif number == guess_me:
#        print("found it!")
#        break
#   elif number > guess_me:
#        print("oops")
#        break
#   number += 1

# -----
#    if number > guess_me:
#        print("oops")
#        break
#    else:
#        print(number + 1)
#        break

for number in range(10):
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
        break
    elif number > guess_me:
        print("oops")
        break
