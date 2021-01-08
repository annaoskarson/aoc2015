import itertools
with open('aoc2015-17-input.txt') as file:
    intext = file.read().strip().split('\n')

containers = [int(x) for x in intext]
results = []

def partone():
    global results
    right = 150
    for i in range(len(containers)):
        t = list(itertools.combinations(containers, i))
        combos = [a for a in t if sum(a) == right]
        results.extend(combos)
    return(len(results))

def parttwo():
    global results
    results = (sorted(results,key=len))
    return(len([len(r) for r in results if len(r) == len(results[0])]))

print('Advent of Code 2015, day 17 part 1')
print(partone())
print('Advent of Code 2015, day 17 part 2')
print(parttwo())
