import itertools

with open('aoc2015-17-input.txt') as file:
    intext = file.readlines()
intext = [line.strip() for line in intext]

containers = [int(x) for x in intext]

right = 150
many = 0
results = []
for i in range(len(containers)-1):
    t = list(itertools.combinations(containers, i))
    for a in t:
        if sum(a) == right:
            results = results + [a]
            many += 1
print("Answer part one:", many)

results = (sorted(results,key=len))
number = 0
for r in results:
    if len(r) == len(results[0]):
        number += 1
    else:
        break

print("Answer part two:", number)
    


