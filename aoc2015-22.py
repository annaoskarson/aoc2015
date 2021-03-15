 # -*- coding: utf-8 -*-
import copy

def init(intext):
    boss = {}
    me = {}
    for line in intext:
        boss[line.split(':')[0]] = int(line.split(':')[1].strip())
        me[line.split(':')[0]] = 0

    me['Hit Points'] = 50
    me['Armor'] = 0
    me['mana'] = 500
    me['effects'] = {'Magic Missile': 0, 'Drain': 0, 'Shield': 0, 'Poison': 0, 'Recharge': 0}
    return(me,boss)

def partone(mode='easy'):
    global goal
    goal = float('inf')

    def turn(me, boss, meturn, totals):
        global goal
        if totals > goal:
            return(float('inf'))

        table = {'Recharge': {'Cost': 229, 'Turns': 5, 'Damage': 0, 'Heal': 0, 'Armor': 0, 'mana': 101},
                'Poison': {'Cost': 173, 'Turns': 6, 'Damage': 3, 'Heal': 0, 'Armor': 0, 'mana': 0},
                'Shield': {'Cost': 113, 'Turns': 6, 'Damage': 0, 'Heal': 0, 'Armor': 7, 'mana': 0},
                'Magic Missile': {'Cost': 53, 'Turns': 1, 'Damage': 4, 'Heal': 0, 'Armor': 0, 'mana': 0},
                'Drain': {'Cost': 73, 'Turns': 1, 'Damage': 2, 'Heal': 2, 'Armor': 0, 'mana': 0}
                }

        if meturn and mode == 'hard':
            me['Hit Points'] -= 1
            if me['Hit Points'] <= 0:
                return(float('inf'))

        # Effects take place
        me['Armor'] = 0
        for eff in me['effects'].keys():
            if me['effects'][eff] > 0:
                me['effects'][eff] -= 1
                boss['Hit Points'] -= table[eff]['Damage']
                me['Hit Points'] += table[eff]['Heal']
                me['Armor'] += table[eff]['Armor']
                me['mana'] += table[eff]['mana']

        # Om bossen har dött, returnera totals
        if boss['Hit Points'] <= 0:
            return(totals)
        # Om mintur
        if meturn:
            # Gör en lista av möjliga spells
            spells = [spell for spell in table.keys() if me['effects'][spell] == 0 and table[spell]['Cost'] <= me['mana']]
            mintotals = float('inf')
            for spell in spells:
                # Ny instans av me, där allt ska hända
                me2 = copy.deepcopy(me)
                # Lägg till effekter
                me2['effects'][spell] = table[spell]['Turns']
                # Betala spell
                me2['mana'] -= table[spell]['Cost']
                boss2 = copy.deepcopy(boss)
                # Skicka med (betalning + totals)
                mintotals = min(mintotals, turn(me2, boss2, False, totals+table[spell]['Cost']))
                goal = min(goal, mintotals)

            # Returnera billigast
            return(mintotals)

        # Om bossens tur
        if not(meturn):
            me['Hit Points'] -= boss['Damage'] - me['Armor']

            # Om me har dött, returnera jättemycket
            if me['Hit Points'] <= 0:
                return(float('inf'))
            else:
                # Om me inte har dött, returnera(turn(nya gubbar, meturn=True, totals))
                return(turn(me, boss, True, totals))

    with open('aoc2015-22-input.txt') as file:
        intext = file.read().strip().split('\n')

    me, boss = init(intext)

    return(turn(me, boss, True, 0))

print('Advent of Code 2015, day 21 part 1')
print(partone())
print('Advent of Code 2015, day 21 part 2')
print(partone('hard'))
