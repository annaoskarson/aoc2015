phrase = '1113122113'

import re, itertools

def talk(ph):
    say = ''
    for num, group in itertools.groupby(ph):
        say += str(len(list(group))) + str(num)

    return(say)

def partone(phrase):
    for i in range(40):
        phrase = talk(phrase)
    return(len(phrase))

def parttwo(phrase):
    for i in range(50):
        phrase = talk(phrase)
    return(len(phrase))

print('Advent of Code 2015, day 10 part 1')
print(partone(phrase))
print('Advent of Code 2015, day 10 part 2')
print(parttwo(phrase))
