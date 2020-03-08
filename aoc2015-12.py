with open('aoc2015-12-input.txt') as file:
    words = file.readlines()

#print(type(words))
#print(len(words))
words = [line.strip() for line in words]

#print(type(words))
#print(len(words))

w = words[0]
#    print(type(w))
#    w = w.split(':')
w = w.replace(':', ',')
w = w.replace('[', ',')
w = w.replace(']', ',')
w = w.replace('{', ',')
w = w.replace('}', ',')
#    print(w[:100])
#    print(w)
#    exit()


w = w.split(',')

add = 0
for s in w:
    if s.lstrip('-+').isdigit():
#    if s.isdigit():
#        print(s, int(s))
        add = add + int(s)
print(add)

#print(words)
#exit()


#partone()
#parttwo()
