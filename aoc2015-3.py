with open('aoc2015-3-input.txt') as file:
    directions = file.readlines()

#directions = [line.strip() for line in directions]
directions = directions[0]
#print(directions)


def partone ():

    houses = set()

    x = 0
    y = 0
    #count = 0
    houses.add((x,y))
    #print(houses)
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
    #print(houses)
    #print(count)

    print('Santa deliviered to', len(houses), 'number of houses.')

def parttwo ():
    hh = set()
    rx = 0
    ry = 0
    sx = 0
    sy = 0
    hh.add((0,0))
    rturn = False
    for d in directions:
        if d == '^':
            if rturn:
                ry += 1
            else:
                sy += 1
        elif d == 'v':
            if rturn:
                ry -= 1
            else:
                sy -= 1
        elif d == '<':
            if rturn:
                rx -= 1
            else:
                sx -= 1
        elif d == '>':
            if rturn:
                rx += 1
            else:
                sx += 1
        if rturn:
            hh.add((rx,ry))
        else:
            hh.add((sx,sy))
        rturn = not(rturn)

    print('They deliviered to', len(hh), 'number of houses.')

partone()
parttwo()


        
