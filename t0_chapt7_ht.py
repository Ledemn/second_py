print('# 7.1')     # 7.1
years_list = [1984, 1985, 1986, 1987, 1988, 1989]
print(years_list)


print('\n', '# 7.2')    # 7.2
print(years_list[3])


print('\n', '# 7.3')    # 7.3
print(years_list[-1])


print('\n', '# 7.4')    # 7.4
things = ["mozzarella", "cinderella", "salmonella"]
print(things)


print('\n', '# 7.5')    # 7.5
print(things[1].capitalize())
# things[1] = things[1].capitalize()
print(things)


print('\n', '# 7.6')    # 7.6
print(things[0].upper())
things[0] = things[0].upper()
print(things)


print('\n', '# 7.7')    # 7.7
things.remove("salmonella")
# del things[-1]
# del things[2]
print(things)


print('\n', '# 7.8')    # 7.8
surprise = ["Groucho", "Chico", "Harpo"]
print(surprise)


print('\n', '# 7.9')    # 7.9
surprise[-1] = surprise[-1].lower()
surprise[-1] = surprise[-1][::-1]
print(surprise[-1].capitalize())


print('\n', '# 7.10')    # 7.10
even = [number for number in range(10) if number % 2 == 0]
print(even)


print('\n', '# 7.11')    # 7.11
start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
    ]
start2 = "Someone better"
# start1_caps = " ".join([word.capitalize() + "!" for word in start1])
for first, second in rhymes:
    # print(f"{start1_caps} {first.capitalize()}!")
    print(f"{first.capitalize()}!_*")
    print(f"{start2} {second}.")
