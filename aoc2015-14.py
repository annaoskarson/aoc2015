with open('aoc2015-14-input.txt') as file:
    text = file.read().strip().split('\n')

deers = {}
for row in text:
    name = row.split(' ')[0]
    speed = int(row.split(' ')[3])
    time = int(row.split(' ')[6])
    rest = int(row.split(' ')[-2])
    deers[name] = [speed, time, rest]

# Test data
#deers = {
#    'Comet': [14, 10, 127],
#    'Dancer': [16, 11, 162]}

def howfar(deer, time): # hur långt en ren tagit sig efter viss tid
    dist = 0
    [v, atime, rtime] = deers[deer]
    ncyc = time // (atime+rtime) # antal hela cykler
    nover = time % (atime+rtime) # resttid, ej hel cykel
    dist = ncyc * (v*atime) # antal cykler * hur långt hen kommer på en cykel
    if nover < atime:
        dist += nover * v # om renen fortfarande rör på sig en stund till
    elif nover >=atime:
        dist += atime * v # renen har nått maxsträcka och vilar nu
    return(dist)

def partone(deers):
    ddist = {} # Hur långt alla renarna kommit
    for d in deers:
        dist = howfar(d, 2504)
        ddist.update({d : dist})
    wd, wdeer = max(zip(ddist.values(), ddist.keys()))
    print(wdeer) # We want to know the name of the winner, of course!
    return(wd)

def parttwo(deers):
    points = {} # Hur många poäng varje ren har
    for d in deers:
        points.update({d : 0})
    for rtime in range(1, 2504): # Kolla varje sekund vilken ren som kommit längst
        ddist = {} # Hur långt varje ren har kommit
        for d in deers: # uppdatera sträckan för alla renar
            dist = howfar(d, rtime)
            ddist.update({d : dist})
        wdist = max(ddist.values()) # Längsta sträckan vinner
        for d in deers: # flera renar kan ligga lika, kolla igenom alla
            if ddist[d] == wdist: # Alla som ligger först får poäng!
                points.update({d : points[d] + 1})

    wp, wdeer = max(zip(points.values(), points.keys()))
    print(wdeer) # We want to know the name of the winner, of course!
    return(wp)

print('Advent of Code 2015, day 14 part 1')
print(partone(deers))
print('Advent of Code 2015, day 14 part 2')
print(parttwo(deers))
