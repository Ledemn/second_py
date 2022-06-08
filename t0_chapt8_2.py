# Chart8: Day3
import copy

print('\n\n', '#018 .DEEPCOPY()', '-' * 39)
# 018-----------------------------------------------
signals = {'green': 'go',
           'yellow': 'go faster',
           'red': ['stop', 'smile']}

signals_copy = copy.deepcopy(signals)

print(signals)
print(signals_copy)

print(signals.keys())  # just 4or practice
print(signals['green'])  # just 4or practice
print(signals['red'])  # just 4or practice

signals['red'][1] = 'sweat'

print(signals)
print(signals_copy)


print('\n\n', '#019 ==, !=', '-' * 44)
# 019-----------------------------------------------
a = {1:1, 2:2, 3:3}
b = {3:3, 1:1, 2:2}
print(a == b)

a = {1: [1, 2], 2: [1], 3:[1]}
b = {1: [1, 1], 2: [1], 3:[1]}
print(a == b)

print(a.values())
print(b.values())
print(list(b.values()))


print('\n\n', '#020 FOR and IN', '-' * 40)
# 020-----------------------------------------------
accusation = {'room': 'ballroom', 'weapon': 'lead pipe',
              'person': 'Col. Mustard'}
print(accusation)

for card in accusation:     # for card in accusation.keys():
    print(card)

print('----')
for value in accusation.values():
    print(value)

print('----')
for item in accusation.items():
    print(item)

print('----')
for card, contents in accusation.items():
    print('Card', card, 'has the contents', contents)


# Chart8: Day4
print('\n\n', '#021 ', '-' * 50)
# 021-----------------------------------------------
word = 'letters'
print(word)

letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)

print('----')
letter_counts = {letter: word.count(letter) for letter in set(word)}
print(letter_counts)


print('\n\n', '#022 ', '-' * 50)
# 022-----------------------------------------------
vowels = 'aeiou'
word = 'onomatopoeia'
print(word)

vowel_counts = {letter: word.count(letter) for letter in set(word)
                if letter in vowels}
print(vowel_counts)
