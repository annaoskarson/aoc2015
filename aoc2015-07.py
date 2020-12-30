with open('aoc2015-07-input.txt') as file:
    lines = file.read().strip().split('\n')

net = {} # Store the operations in the net
for l in lines:
    if 'NOT' in l:
        com, a1, _, d = l.split(' ')
        value = [com, a1, '']
    elif 'AND' in l or 'OR' in l or 'SHIFT' in l:
        a1, com, a2, _, d = l.split(' ')
        value = [com, a1, a2]
    else:
        a1, _, d = l.split(' ')
        value = ['VAL', a1, '']
    net[d] = value

result = {} # Store the values of the net
def solve(gate):

    # Here comes the dynamic programming!
    global result
    if gate in result.keys():
        return(result[gate])

    [com, a1, a2] = net[gate]
    if com == 'VAL':
        if a1.isdigit():
            val = int(a1)
        else:
            val = solve(a1)
    elif com == 'NOT':
        if a1.isdigit():
            val = ~int(a1)&65535 # May be negative
        else:
            val = ~solve(a1)&65535 # May be negative
    elif com == 'AND':
        if a1.isdigit():
            val = int(a1)&solve(a2)
        elif a2.isdigit():
            val = solve(a1)&int(a2)
        else:
            val = solve(a1)&solve(a2)
    elif com == 'OR':
        val = solve(a1)|solve(a2)
    elif com == 'RSHIFT':
        val = solve(a1)>>int(a2)
    elif com == 'LSHIFT':
        val = (solve(a1)<<int(a2))&65535 # May be negative

    result[gate] = val
    return(val)

def partone():
    return(solve('a'))

def parttwo():
    global result
    thenewb = result['a']
    result = {}
    result['b'] = thenewb
    return(solve('a'))

print('Advent of Code 2015, day 7 part 1')
print(partone())
print('Advent of Code 2015, day 7 part 2')
print(parttwo())
