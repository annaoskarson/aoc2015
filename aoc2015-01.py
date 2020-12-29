
with open('aoc2015-01-input.txt', 'r') as f:
  path = f.read().strip()

def partone():
    return(path.count('(') - path.count(')'))

def parttwo():
    i, floor = 0, 0
    while floor >= 0:
        if path[i] == '(':
            floor += 1
        elif path[i] == ')':
            floor -= 1
        i += 1
    return(i)

print('Advent of Code 2015, day 1 part 1')
print(partone())
print('Advent of Code 2015, day 1 part 2')
print(parttwo())
