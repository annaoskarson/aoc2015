with open('aoc2015-03-input.txt') as file:
    directions = file.read()

def partone (directions):
    houses = set()

    x = 0
    y = 0
    houses.add((x,y))
    for d in directions:
        if d == '^':
            y += 1
        elif d == 'v':
            y -= 1
        elif d == '<':
            x -= 1
        elif d == '>':
            x += 1
        houses.add((x,y))
    return(houses)

def parttwo ():
    houses = set()
    houses.add((0,0))
    santa = directions[::2]
    robot = directions[1::2]
    houses = partone(santa) | partone(robot)
    return(houses)

print('Advent of Code 2015, day 3 part 1')
print(len(partone(directions)))
print('Advent of Code 2015, day 3 part 2')
print(len(parttwo()))
