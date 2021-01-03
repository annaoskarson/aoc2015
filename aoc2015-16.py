with open('aoc2015-16-input.txt') as file:
    intext = file.read().strip().split('\n')

#print(intext)

sues = {}
for text in intext:
    sue = text.split(':',1)[0]
    stuff = text.split(' ',2)[2].split(',')
    things = []
    sues[sue] = {}
    for a in stuff:
        (item, number) = a.strip().split(':')
        sues[sue][item] = int(number)

def partone():

    def checksue(aunt):
        checklist = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}
        return(all([checklist[item] == sues[aunt][item] for item in sues[aunt].keys()]))

    return(next(sue for sue in sues.keys() if checksue(sue)))

def parttwo():

    def checksue(aunt):

        def checkitem(item):
            if item in ['cats', 'trees']:
                return(checklist[item] < sues[aunt][item])
            elif item in ['pomeranians', 'goldfish']:
                return(checklist[item] > sues[aunt][item])
            else:
                return(checklist[item] == sues[aunt][item])

        checklist = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}
        return(all([checkitem(thing) for thing in sues[aunt].keys()]))

    return(next(sue for sue in sues.keys() if checksue(sue)))

print('Advent of Code 2015, day 16 part 1')
print(partone())
print('Advent of Code 2015, day 16 part 2')
print(parttwo())
