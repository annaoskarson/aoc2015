
with open('aoc2015-02-input.txt', 'r') as f:
    dimensions = f.read().strip().split('\n')

paper = 0
ribbon = 0
for one in dimensions:
    [l,w,h] = list(map(int, one.split('x')))
    paper += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
    box = [l,w,h]
    ribbon += sorted(box)[0]*2 + sorted(box)[1]*2 + l*w*h

print('Advent of Code 2015, day 2 part 1')
print(paper)
print('Advent of Code 2015, day 2 part 2')
print(ribbon)
