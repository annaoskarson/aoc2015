with open('aoc2015-18-input.txt') as file:
    intext = file.read().strip().split('\n')

# Initialize
def init(text):
    global size
    size = len(text)
    lightson = set()
    for y,row in enumerate(intext):
        for x,light in enumerate(row):
            if light == '#':
                lightson.add((x,y))
    return(lightson)

def adjacent(coord):
    global size
    x,y = coord
    adj = []
    # return list of up to eight
    for xn in [x-1, x, x+1]:
        for yn in [y-1, y, y+1]:
            if -1 < xn < size+1 and -1 < yn < size+1 and (xn, yn) != (x,y):
                adj.append((xn,yn))
    return(adj)

#A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
#A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
def change(ll):

    def turnoff(l):
        # First, list the neighbors which are on.
        n_on = [nl for nl in adjacent(l) if nl in ll]
        if not(len(n_on) in [2,3]):
            return(True)

    def turnon(l):
        # First, list the neighbors which are on.
        n_on = [nl for nl in adjacent(l) if nl in ll]
        if len(n_on) == 3:
            return(True)

    add_l = set()
    del_l = set()
    for y in range(size):
        for x in range(size):
            if (x,y) in ll and turnoff((x,y)):
                del_l.add((x,y))
            elif (x,y) not in ll and turnon((x,y)):
                add_l.add((x,y))
    return(ll.union(add_l).difference(del_l))

def partone():
    lights = init(intext) # Make initial configuration.
    for i in range(100): # Try 100 changes.
        lights = change(lights)
    return(len(lights))

def parttwo():
    corners = {(0,0),(0,size-1),(size-1,0),(size-1,size-1)}
    # Corners are stuck on.
    lights = init(intext).union(corners)
    for i in range(100):
        lights = change(lights).union(corners)
    return(len(lights))

print('Advent of Code 2015, day 18 part 1')
print(partone())
print('Advent of Code 2015, day 18 part 2')
print(parttwo())
