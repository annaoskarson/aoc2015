with open('aoc2015-16-input.txt') as file:
    intext = file.readlines()

intext = [line.strip() for line in intext]

sues = {}
for text in intext:
    type(text)
#    print(text)
    text = text.split(':',1)
    sue = text[0]
    text = text[1]
    text2 = text.split(',')
    things = []
    for a in text2:
        (item, number) = a.strip().split(':')
        things += [(item, int(number))]
    sues[sue] = things
#print(sues)


# Kolla om grejerna i listan stämmer. Om varje grej stämmer alternativt inte finns alls, så är det rätt Sue.

for sue in sues:
    children = False
    cats = False
    samoyeds = False
    pomeranians = False
    akitas = False
    vizslas = False
    goldfish = False
    trees = False
    cars = False
    perfumes = False
    for thing in sues[sue]:
#        print(thing)
        if thing[0] == 'children':
            children = (thing[1] == 3)
        elif thing[0] == 'cats':
            cats = (thing[1] == 7)
        elif thing[0] == 'samoyeds':
            samoyeds = (thing[1] == 2)
        elif thing[0] == 'pomeranians':
            pomeranians = (thing[1] == 3)
        elif thing[0] == 'akitas':
            akitas = (thing[1] == 0)
        elif thing[0] == 'vizslas':
            vizslas = (thing[1] == 0)
        elif thing[0] == 'goldfish':
            goldfish = (thing[1] == 5)
        elif thing[0] == 'trees':
            trees = (thing[1] == 3)
        elif thing[0] == 'cars':
            cars = (thing[1] == 2)
        elif thing[0] == 'perfumes':
            perfumes = (thing[1] == 1)
            
#    print(children, cats, samoyeds, pomeranians, akitas, vizslas, goldfish, trees, cars, perfumes)
    print(cats)
    if children:
        print('children', sue)
    if children and cats and samoyeds and pomeranians:
        print(sue)
#    print(children)
#    print(thing[0])

#partone()
#parttwo()
