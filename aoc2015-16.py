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



def partone():
    def checksue(aunt):
        checklist = [('children', 3), ('cats', 7), ('samoyeds', 2), ('pomeranians', 3), ('akitas', 0), ('vizslas', 0), ('goldfish', 5), ('trees', 3), ('cars', 2), ('perfumes', 1)]
        results = []
        for check in checklist:
            if [item for item in sues[aunt] if item == check] or not [item for item in sues[aunt] if item[0] == check[0]]:
                pass
#                results = results + [True]
            else:
                return(False)
#        print(results)
        return(True)

    for sue in sues:
        if checksue(sue):
            print('The right aunt is', sue)

def parttwo():
    def checksue(aunt):
        checklist = [('children', 3), ('cats', 7), ('samoyeds', 2), ('pomeranians', 3), ('akitas', 0), ('vizslas', 0), ('goldfish', 5), ('trees', 3), ('cars', 2), ('perfumes', 1)]
        results = []
        print(results)
        for check in checklist:
            if not [item for item in sues[aunt] if item[0] == check[0]]:
#            if check[0] not in sues[aunt]:
#                print(check, 'not in', sues[aunt])
                return(False)
            else:
                #leta upp check hos sues[aunt] ...
                for item in sues[aunt]:
                    if check[0] == item[0]:
                        if check[0] in ['cats', 'trees']:
                            results = results + [item[1] > check[1]]
                        elif check[0] in ['pomeranians', 'goldfish']:
                            results = results + [item[1] < check[1]]
                        else:
                            results = results + [item[1] == check[1]]
    #                else:
    #                    results = results + [False]

        print(results)
        return(all(results))
    
##            if [item for item in sues[aunt] if item[0] == check[0]]:
##                if check[0] == 'children':
##                    sues[aunt
##                or not [item for item in sues[aunt] if item[0] == check[0]]:
##                pass
###                results = results + [True]
##            else:
##                return(False)
###        print(results)
##        return(True)

    for sue in sues:
        print(sue)
        if checksue(sue):
            print('The right aunt is', sue)

#partone()
parttwo()
