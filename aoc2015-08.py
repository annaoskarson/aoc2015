with open('aoc2015-08-input.txt') as file:
    code = file.read().strip().split('\n')

def partone(text):
    tsize = 0
    csize = 0
    for c in code:
        csize += len(c)
        tsize += len(eval(c))
        # eval() will interpret the string

    return(csize-tsize)

import json
def parttwo(text):
    asize = 0
    bsize = 0
    for c in code:
        asize += len(c)
        bsize += len(json.dumps(c))
        # found out that json.dumps() did the job after thorough search on the web
    return(bsize-asize)

print('Advent of Code 2015, day 8 part 1')
print(partone(code))
print('Advent of Code 2015, day 8 part 2')
print(parttwo(code))
