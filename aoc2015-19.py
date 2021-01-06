import re
with open('aoc2015-19-input.txt') as file:
    intext = file.read().strip().split('\n')

table = {}
translation = set()
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
        translation.add((fr,to))

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
    global translation
    translation = sorted(translation, reverse = True, key = lambda x: len(x[1]))

    m = molecule
    num = 0

    def doit(m, num):
        # Testa först med de längsta "svaren"
        for tr in translation:
            num += m.count(tr[1])
            # Substituera och fortsätt
            m = m.replace(tr[1], tr[0])
        return(m, num)

    # Kolla om man till slut kan komma ända fram ...
    while m != 'e':
        m, num = doit(m, num)
    return(num)

print('Advent of Code 2015, day 19 part 1')
print(partone())
print('Advent of Code 2015, day 19 part 2')
print(parttwo())
