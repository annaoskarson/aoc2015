import json

with open('aoc2015-12-input.txt') as f:
  data = json.load(f)

#data = [1,{"c":"red","b":2},3]
#data = {"d":"red","e":[1,2,3,4],"f":5}
#data = [1,"red",5]

def partone(data):
    w = json.dumps(data)
    w = w.replace(':', ',').replace('[', ',').replace(']', ',').replace('{', ',').replace('}', ',').replace('"', '')
    w = list(map(str.strip, w.split(',')))

    sum = 0
    for s in w:
        if s.lstrip('-+').isdigit():
            sum += int(s)
    return(sum)

def parttwo(data):

    def countnotred(d):
        if type(d) == type(1):
            return(d)
        elif type(d) == type([]): # Alla listor oavsett innehåll ska kollas.
            return(sum([countnotred(item) for item in d]))
        elif type(d) == type(dict()) and 'red' not in d.values(): # Alla dictionoaries som inte innehåller värdet 'red' ska kollas.
            return(sum([countnotred(item) for item in d.values()]))
        else:
            return(0)

    red = countnotred(data)
    return(red)

print('Advent of Code 2015, day 12 part 1')
print(partone(data))
print('Advent of Code 2015, day 12 part 2')
print(parttwo(data))
