##Dancer can fly 27 km/s for 5 seconds, but then must rest for 132 seconds.
##Cupid can fly 22 km/s for 2 seconds, but then must rest for 41 seconds.
##Rudolph can fly 11 km/s for 5 seconds, but then must rest for 48 seconds.
##Donner can fly 28 km/s for 5 seconds, but then must rest for 134 seconds.
##Dasher can fly 4 km/s for 16 seconds, but then must rest for 55 seconds.
##Blitzen can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.
##Prancer can fly 3 km/s for 21 seconds, but then must rest for 40 seconds.
##Comet can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.
##Vixen can fly 18 km/s for 5 seconds, but then must rest for 84 seconds.

deers = {
    'Dancer': [27, 5, 132],
    'Cupid': [22, 2, 41],
    'Rudolph': [11, 5, 48],
    'Donner': [28, 5, 134],
    'Dasher': [4, 16, 55],
    'Blitzen': [14, 3, 38],
    'Prancer': [3, 21, 40],
    'Comet': [18, 6, 103],
    'Vixen': [18, 5, 84]}

# Test data
#deers = {
#    'Comet': [14, 10, 127],
#    'Dancer': [16, 11, 162]}


def howfar(deer, time): # hur långt en ren tagit sig efter viss tid
    dist = 0
    [v, a, b] = deers[deer]
    if time > a+b:
        t = time // (a+b) # antal hela cykler
        n = time % (a+b) # resttid
        dist = t * (v*a) # antal cykler * hur långt man kommer på en cykel
        if n < a:
            dist += n * v
        elif n >=a:
            dist += a * v
    elif time < a: # om man inte tar sig förbi hela a-tiden
        dist = time * v
    elif time >= a: # om man hamnar på första b-tiden (har stannat)
        dist = a * v
    return(dist)

def partone(deers):
    ddist = {}
    for d in deers:
        dist = howfar(d, 2504)
        ddist.update({d : dist})
    (wd, wdeer) = (max(zip(ddist.values(), ddist.keys())))
    print('Part one:', wdeer, 'is the winner by distance with', wd, 'km.')

def parttwo(deers):
    points = {}
    for d in deers:
        points.update({d : 0})
    for rtime in range(1, 2504):
        ddist = {}
        for d in deers: # uppdatera sträckan för alla hästar
            dist = howfar(d, rtime)
            ddist.update({d : dist})
        wdist = max(ddist.values())
        for d in deers: # flera hästar kan ligga lika, kolla igenom alla
            if ddist[d] == wdist:
                points.update({d : points[d] + 1})
                
    (wp, wdeer) = (max(zip(points.values(), points.keys())))
    print('Part two:', wdeer, 'is the winner by points with', wp, 'points.')

partone(deers)
parttwo(deers)
