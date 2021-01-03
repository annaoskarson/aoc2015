with open('aoc2015-15-input.txt') as file:
    text = file.read().strip().split('\n')

# Test data
#text = ['Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8', 'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3']

facts = {}
for row in text:
    #print(row)
    ing = row.split(':')[0]
    _, _, capacity, _, durability, _, flavor,_, texture, _, calories = row.replace(',', '').split(' ')
    facts[ing] = {'capacity': int(capacity), 'durability': int(durability), 'flavor': int(flavor), 'texture': int(texture), 'calories': int(calories)}

# This is not a good, nor a fast way to fix some recipes ... But I just wanted to get the right answer ...
var = []
for i in range(1, 100):
    for j in range(1, 100):
        for k in range(1, 100):
            l = 100-k-j-i
            var.append([i,j,k,l])

def score(recipe):
    global facts
    score = 1
    points = list(facts[list(facts.keys())[0]].keys())[:-1]
    for comp in points:
        onescore = sum([recipe[ingred] * facts[ingred][comp] for ingred in facts.keys()])
        if onescore < 0:
            onescore = 0
        score *= onescore
    return(score)

def partone():

    highscore = 0
    for v in var:
        recipe = {}
        a = 0
        for i in facts.keys():
            recipe.update({i : v[a]})
            a += 1
        highscore = max(highscore, score(recipe))
    return(highscore)

def calories(recipe):
    cal = sum([recipe[ingred] * facts[ingred]['calories'] for ingred in facts.keys()])
    return(cal)

def parttwo():
    highscore = 0
    for v in var:
        recipe = {}
        a = 0
        for i in facts.keys():
            recipe.update({i : v[a]})
            a += 1
        if calories(recipe) == 500:
            highscore = max(highscore, score(recipe))
    return(highscore)


print('Advent of Code 2015, day 15 part 1')
print(partone())
print('Advent of Code 2015, day 15 part 2')
print(parttwo())
