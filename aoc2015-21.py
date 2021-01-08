with open('aoc2015-21-input.txt') as file:
    intext = file.read().strip().split('\n')

#print(intext)
def init():
    boss = {}
    me = {}
    for line in intext:
        boss[line.split(':')[0]] = int(line.split(':')[1].strip())
        me[line.split(':')[0]] = 0

    me['Hit Points'] = 100
    return(me,boss)

shop = {'Weapons':
{'Dagger': {'Cost': 8, 'Damage': 4, 'Armor': 0},
'Shortsword': {'Cost': 10, 'Damage': 5, 'Armor': 0},
'Warhammer': {'Cost': 25, 'Damage': 6, 'Armor': 0},
'Longsword': {'Cost': 40, 'Damage': 7, 'Armor': 0},
'Greataxe': {'Cost': 74, 'Damage': 8, 'Armor': 0}},
'Armor':
{'Leather': {'Cost': 13, 'Damage': 0, 'Armor': 1},
'Chainmail': {'Cost': 31, 'Damage': 0, 'Armor': 2},
'Splintmail': {'Cost': 53, 'Damage': 0, 'Armor': 3},
'Bandedmail': {'Cost': 75, 'Damage': 0, 'Armor': 4},
'Platemail': {'Cost': 102, 'Damage': 0, 'Armor': 5}},
'Rings':
{'Damage +1': {'Cost': 25, 'Damage': 1, 'Armor':0},
'Damage +2': {'Cost': 50, 'Damage': 2, 'Armor':0},
'Damage +3': {'Cost': 100, 'Damage': 3, 'Armor':0},
'Defense +1': {'Cost': 20, 'Damage': 0, 'Armor':1},
'Defense +2': {'Cost': 40, 'Damage': 0, 'Armor':2},
'Defense +3': {'Cost': 80, 'Damage': 0, 'Armor':3}}}

def fight(attacker, defender):
    defender['Hit Points'] -= max((attacker['Damage'] - defender['Armor']), 1)
    return(attacker, defender)

def win(p1, p2):
    turn = 1
    #print('player',p1)
    while p1['Hit Points'] > 0 and p2['Hit Points'] > 0:
        if turn == 1:
            p1, p2 = fight(p1, p2)
            turn = 2
        else:
            p2, p1 = fight(p2, p1)
            turn = 1
    if p1['Hit Points'] > 0:
        return(True)

# Test data
#me = {'Hit Points': 8, 'Damage': 5, 'Armor': 5}
#boss = {'Hit Points': 12, 'Damage': 7, 'Armor': 2}
#print(me, boss)

def buy(items, me):
    p = 0
    for item in items:
        if item in shop['Weapons'].keys():
            cda = shop['Weapons'][item]
        elif item in shop['Armor'].keys():
            cda = shop['Armor'][item]
        elif item in shop['Rings'].keys():
            cda = shop['Rings'][item]
        #print(cda)
        p += cda['Cost']
        me['Damage'] += cda['Damage']
        me['Armor'] += cda['Armor']
    return(p, me)

def partone():
    def match(items):
        me, boss = init()
        spent, me = buy(items, me)
        if win(me, boss):
            return(spent)
        else:
            return(1000) # A high cost ...
    #You must buy exactly one weapon; no dual-wielding.
    #Armor is optional, but you can't use more than one.
    #You can buy 0-2 rings (at most one for each hand). You must use any items you buy.
    #The shop only has one of each item, so you can't buy, for example, two rings of Damage +3.
    cost = 1000 #Start with a high cost ...
    for w in shop['Weapons']:
        cost = min(match([w]), cost)
        for a in shop['Armor']:
            cost = min(match([w,a]), cost)
            for r1 in shop['Rings'].keys():
                cost = min(match([w,a,r1]), cost)
                cost = min(match([w,r1]), cost)

                for r2 in [x for x in shop['Rings'] if x != r1]:
                    cost = min(match([w,a,r1,r2]), cost)
                    cost = min(match([w,r1,r2]), cost)
    return(cost)

def parttwo():
    def match(items):
        me, boss = init()
        spent, me = buy(items, me)
        if not win(me, boss): #This time, we shall lose.
            return(spent)
        else:
            return(0)
    cost = 0 #Start with a low cost ...
    for w in shop['Weapons']:
        cost = max(match([w]), cost)
        for a in shop['Armor']:
            cost = max(match([w,a]), cost)
            for r1 in shop['Rings'].keys():
                cost = max(match([w,a,r1]), cost)
                cost = max(match([w,r1]), cost)

                for r2 in [x for x in shop['Rings'] if x != r1]:
                    cost = max(match([w,a,r1,r2]), cost)
                    cost = max(match([w,r1,r2]), cost)
    return(cost)


print('Advent of Code 2015, day 21 part 1')
print(partone())
print('Advent of Code 2015, day 21 part 2')
print(parttwo())
