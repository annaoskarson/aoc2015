oldpass = 'hepxcrrq'

def incr(w):
    w[-1] += 1
    if w[-1] > ord('z'):
        w[-1] = ord('a')
        w = incr(w[:-1]) + [ord('a')]
    return(w)

def valid(w):
    return(pairs(w) and threestraight(w) and not nopeletter(w))

def nopeletter(w):
    return(any(c in w for c in [ord('i'), ord('o'), ord('l')]))

def threestraight(w):
    return(any(w[i]+2 == w[i+1]+1 == w[i+2] for i in range(len(w)-2)))

def pairs(w):
    for i in range(len(w)-1):
        for j in range(i+2, len(w)-1):
            if w[i] == w[i+1] and w[j] == w[j+1]:
                return(True)

def type(w):
    return(''.join(map(chr, w)))

def partone(passwd):
    w = [ord(i) for i in list(passwd)]
    w = incr(w)
    while not valid(w):
        w = incr(w)
    return(type(w))

print('Advent of Code 2015, day 11 part 1')
print(partone(oldpass))
print('Advent of Code 2015, day 11 part 2')
print(partone(partone(oldpass)))
