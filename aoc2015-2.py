with open('aoc2015-2-input.txt') as file:
    dimensions = file.readlines()

dimensions = [line.strip() for line in dimensions]
#dimensions = ['2x3x4']

#print(dimensions)
totalp = 0
totalr = 0
for one in dimensions:
    one = one.split('x')
    #print(one)
    l,w,h = int(one[0]), int(one[1]), int(one[2])
    paper = 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
    totalp = totalp + paper
    box = [l,w,h]
    ribbon = sorted(box)[0]*2 + sorted(box)[1]*2 + l*w*h
#    print(sorted(box))
#    print(ribbon)
    totalr = totalr + ribbon

print('The amount of paper is', totalp, 'squarefeet.')
print('The amount of ribbon is', totalr, 'feet.')


        
