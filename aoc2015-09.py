with open('aoc2015-09-input.txt') as file:
    text = file.read().strip().split('\n')

import itertools

# Test data
#text = ['London to Dublin = 464','London to Belfast = 518','Dublin to Belfast = 141']

map = {}
for road in text:
    [c1, c2, d] = road.split(' ')[0:3:2] + [int(road.split(' ')[4])]
    if c1 not in map.keys():
        map[c1] = {}
    if c2 not in map.keys():
        map[c2] = {}
    map[c1][c2] = d
    map[c2][c1] = d

distance = []

def partone():
    ways = list(itertools.permutations(map.keys()))

    for way in ways:
        dist = 0
        for i,c in enumerate(way[:-1]):
            dist += map[c][way[i+1]]
        distance.append(dist)
    return(min(distance))

def parttwo():
    return(max(distance))

print('Advent of Code 2015, day 9 part 1')
print(partone()) #283 too high
print('Advent of Code 2015, day 9 part 2')
print(parttwo())
