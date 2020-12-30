import re
with open('aoc2015-06-input.txt') as file:
    lines = file.read().strip().split('\n')

    cmds = []

    for c in lines:
        [start, end] = (re.findall(r'\d+,\d+', c))
        x1, y1 = map(int, start.split(','))
        x2, y2 = map(int, end.split(','))
        if 'on' in c:
            cmds.append([(x1,y1),(x2,y2),'on'])
        elif 'off' in c:
            cmds.append([(x1,y1),(x2,y2), 'off'])
        elif 'toggle' in c:
            cmds.append([(x1,y1),(x2,y2), 'tog'])

def partone():
    lighted = set()

    def turnon(start,end):
        (x1,y1) = start
        (x2,y2) = end
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                lighted.add((x,y))

    def toggle(start,end):
        (x1,y1) = start
        (x2,y2) = end
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if (x,y) in lighted:
                    lighted.remove((x,y))
                else:
                    lighted.add((x,y))

    def turnoff(start,end):
        (x1,y1) = start
        (x2,y2) = end
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if (x,y) in lighted:
                    lighted.remove((x,y))

    for c in cmds:
        ((x1,y1),(x2,y2), act) = c
        if act == 'on':
            turnon((x1,y1),(x2,y2))
        elif act == 'off':
            turnoff((x1,y1),(x2,y2))
        elif act == 'tog':
            toggle((x1,y1),(x2,y2))
    return(len(lighted))

def parttwo():
    lights = {}

    def turnon(start,end):
        (x1,y1) = start
        (x2,y2) = end
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if (x,y) in lights:
                    lights[(x,y)] += 1
                else:
                    lights[(x,y)] = 1

    def toggle(start,end):
        (x1,y1) = start
        (x2,y2) = end
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if (x,y) in lights:
                    lights[(x,y)] += 2
                else:
                    lights[(x,y)] = 2

    def turnoff(start,end):
        (x1,y1) = start
        (x2,y2) = end
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if (x,y) in lights and lights[(x,y)] > 1:
                    lights[(x,y)] -= 1
                else:
                    lights.pop((x,y), None)

    for c in cmds:
        ((x1,y1),(x2,y2), act) = c
        if act == 'on':
            turnon((x1,y1),(x2,y2))
        elif act == 'off':
            turnoff((x1,y1),(x2,y2))
        elif act == 'tog':
            toggle((x1,y1),(x2,y2))

    return(sum(lights.values()))


print('Advent of Code 2015, day 6 part 1')
print(partone())
print('Advent of Code 2015, day 6 part 2')
print(parttwo())
