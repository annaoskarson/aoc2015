qrow = 2947
qcol = 3029

def nv(p):
    return((p*252533)%33554393)

def value(row, col):
    val = 20151125
    result = {}
    for max in range(1, qrow+qcol):
        r = max
        c = 1

        while r > 0:
            result[(r,c)] = val

            val = nv(val)
            r -= 1
            c += 1

    return(result)

def partone():
    return(value(qrow, qcol)[(qrow,qcol)])

print('Advent of Code 2015, day 25 part 1')
print(partone())
