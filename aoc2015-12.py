with open('aoc2015-12-input.txt') as file:
    words = file.readlines()

words = [line.strip() for line in words]


w = words[0]
w = w.replace(':', ',')
w = w.replace('[', ',')
w = w.replace(']', ',')
w = w.replace('{', ',')
w = w.replace('}', ',')

w = w.split(',')

add = 0
for s in w:
    if s.lstrip('-+').isdigit():
        add = add + int(s)
print(add)

#partone()
#parttwo()
