with open('aoc2015-24-input.txt') as file:
    intext = file.read().strip().split('\n')

import itertools

ws = set(int(x) for x in intext)

# Test data
#ws = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11][::-1]

def weight(g):
    return(sum(g))

def EQ(g):
    prod = 1
    for p in g:
        prod *= p
    return(prod)

def size(g):
    return(len(g))

def twoequal(g): # Check if g could be split into two equally heavy heaps.
    if sum(g) % 2 != 0: # Cannot split into two.
        return(False)
    for L in range(1, len(g)+1):
        for sublist in itertools.combinations(g, L):
            if sum(sublist) == sum(g)/2:
                return(True)

def partone():
    result = [ws, len(ws)//2, EQ(ws)]
    for L in range(1, len(ws)+1):
        if L > result[1]:
            return(result[2])
        for front in itertools.combinations(ws, L):
            if weight(front) == weight(ws)/3 and twoequal(set(ws)-set(front)):
                if size(front) < result[1]:
                    result = [front, size(front), EQ(front)]
                elif size(front) == result[1] and EQ(front) < result[2]:
                    result = [front, size(front), EQ(front)]
    return(result[2])

def threeequal(g): # Check if g could be split into three equally heavy heaps.
    if sum(g) % 3 != 0: # Cannot split into three.
        return(False)
    for L in range(1, len(g)+1):
        for left in itertools.combinations(g, L):
            if sum(left) == sum(g)/3:
                right = set(g) - set(left)
                for K in range(1, len(right)+1):
                    for middle in itertools.combinations(right, K):
                        if sum(middle) == sum(g)/3:
                            right = right - set(middle)
                            return(True)

def parttwo():
    result = [ws, len(ws)//2, EQ(ws)]
    for L in range(1, len(ws)+1):
        if L > result[1]:
            return(result[2])
        for front in itertools.combinations(ws, L):
            if weight(front) == weight(ws)/4 and threeequal(set(ws)-set(front)):
                if size(front) < result[1]:
                    result = [front, size(front), EQ(front)]
                elif size(front) == result[1] and EQ(front) < result[2]:
                    result = [front, size(front), EQ(front)]
    return(result[2])

print('Advent of Code 2015, day 24 part 1')
print(partone())
print('Advent of Code 2015, day 24 part 2')
print(parttwo())
