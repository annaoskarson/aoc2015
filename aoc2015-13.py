with open('aoc2015-13-input.txt') as file:
    text = file.read().strip().split('\n')

import itertools

seating = {}
for row in text:
    person = row.split(' ')[0]
    units = int(row.split(' ')[3])
    if 'lose' in row:
        units = -units
    neighbor = row.split(' ')[-1][:-1]
    if person not in seating.keys():
        seating[person] = {}

    seating[person][neighbor] = units

#combos = list(itertools.permutations(seating.keys()))
# Some of the combos are the same, since it is a circular table, but I don't mind.

persons = list(seating.keys())
combos = [[persons[0]] + list(ll) for ll in list(itertools.permutations(persons[1:]))]
# This way we only get twice as many combinations as we need, still have the mirroring left ...

# Get rid of the mirrored seatings.
for c in combos:
    c = [c[0]] + c[::-1][:-1] # Reversed list, but keep old first item first.
    if c in combos:
        combos.remove(c)

def points(persons):
    global seating
    i = 0
    points = 0
    while i < len(persons):
        p = persons[i]
        if i == 0:
            n1 = persons[-1]
        else:
            n1 = persons[i-1]

        if i == len(persons)-1:
            n2 = persons[0]
        else:
            n2 = persons[i+1]
        points += seating[p][n1] + seating[p][n2]
        i += 1
    return(points)

def partone():
    return(max([points(combo) for combo in combos]))

def parttwo():
    global seating
    addseating = {}
    for p in seating.keys():
        seating[p]['me'] = 0
        addseating[p] = 0
    seating['me'] = addseating

    combos = list(itertools.permutations(seating.keys()))
    return(max([points(combo) for combo in combos]))

print('Advent of Code 2015, day 13 part 1')
print(partone())
print('Advent of Code 2015, day 13 part 2')
print(parttwo())
