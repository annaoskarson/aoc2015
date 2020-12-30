with open('aoc2015-05-input.txt') as file:
    words = file.read().strip().split('\n')

def partone():
    def threevow(word):
        return(len([c for c in word if c in 'aeiou']) > 2)
    def twoinrow(word):
        return(any(word[i]==word[i+1] for i in range(len(word)-1)))
    def nopestrings(word):
        return(any(x in word for x in ['ab','cd', 'pq', 'xy']))

    return(len([w for w in words if not(nopestrings(w)) and threevow(w) and twoinrow(w)]))

def parttwo():
    def twicetwice(word):
        i = 0
        while i < len(word)-3:
            j = i+2
            #testa två bokstäver (vid i) med resten av strängen (vid j)
            while j < len(word)-1:
                if word[i:i+2] == word[j:j+2]:
                    return(True)
                else:
                    j += 1
            i += 1

    def onebetween(word):
        return(any(word[i] == word[i+2] for i in range(len(word)-2)))

    return(len([w for w in words if onebetween(w) and twicetwice(w)]))

print('Advent of Code 2015, day 2 part 1')
print(partone())
print('Advent of Code 2015, day 2 part 2')
print(parttwo())
