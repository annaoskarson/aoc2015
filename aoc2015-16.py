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

def partone():
    def checksue(aunt):
        checklist = [('children', 3), ('cats', 7), ('samoyeds', 2), ('pomeranians', 3), ('akitas', 0), ('vizslas', 0), ('goldfish', 5), ('trees', 3), ('cars', 2), ('perfumes', 1)]
        results = []
        for check in checklist:
            if [item for item in sues[aunt] if item == check] or not [item for item in sues[aunt] if item[0] == check[0]]:
                pass
            else:
                return(False)
        return(True)

    for sue in sues:
        if checksue(sue):
            print('Part one: The right aunt is', sue)

def parttwo():
    def checksue(aunt):
        def checkitem(machine, my):
            if machine[0] == my[0]:
                if machine[0] in ['cats', 'trees']:
                    return(my[1] > machine[1])
                elif machine[0] in ['pomeranians', 'goldfish']:
                    return(my[1] < machine[1])
                else:
                    return(my[1] == machine[1])

        checklist = [('children', 3), ('cats', 7), ('samoyeds', 2), ('pomeranians', 3), ('akitas', 0), ('vizslas', 0), ('goldfish', 5), ('trees', 3), ('cars', 2), ('perfumes', 1)]
        result = []
        for check in checklist:
            if [item for item in sues[aunt] if item[0] == check[0]]:
                [aitem] = [item for item in sues[aunt] if item[0] == check[0]]
                result = result + [checkitem(check, aitem)]
            else:
                result = result + [True]
        return(all(result))

    for sue in sues:
        if checksue(sue):
            print('Part two: The right aunt is', sue)

partone()
parttwo()
