with open('aoc2015-02-input.txt') as file:
    dimensions = file.readlines()

dimensions = [line.strip() for line in dimensions]

totalp = 0
totalr = 0
for one in dimensions:
    one = one.split('x')
    l,w,h = int(one[0]), int(one[1]), int(one[2])
    paper = 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
    totalp = totalp + paper
    box = [l,w,h]
    ribbon = sorted(box)[0]*2 + sorted(box)[1]*2 + l*w*h
    totalr = totalr + ribbon

print('Part one: The amount of paper is', totalp, 'squarefeet.')
print('Part two: The amount of ribbon is', totalr, 'feet.')
