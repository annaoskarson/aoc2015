import re
with open('aoc2015-19-input.txt') as file:
    intext = file.read().strip().split('\n')

#print(intext)

table = {}
for i,row in enumerate(intext):
    if row == '':
        molecule = intext[i+1]
        break
    else:
        #print(row)
        fr, _, to = row.split(' ')
        if fr not in table:
            table[fr] = []
        table[fr].append(to)

#print(molecule)
#print(table)

def partone():
    alt = set()
    for part in table.keys(): # Kolla varje grundämne
        for sub in table[part]: # Kolle igenom listan av vad grundämnet kan bli
            for match in re.finditer(part, molecule): # Testa att byta ut en gång på varje ställe i molekylen
                start = match.start()
                end = match.end()
                new_mol=''.join((molecule[:start],sub,molecule[end:]))
                alt.add(new_mol) # In med nya molekylen i ett set (unika molekyler).
    return(len(alt))

def parttwo():
    return(0)

print('Advent of Code 2015, day 19 part 1')
print(partone())
print('Advent of Code 2015, day 19 part 2')
print(parttwo())
