with open('aoc2015-5-input.txt') as file:
    words = file.readlines()

words = [line.strip() for line in words]
#directions = directions[0]
#print(words)
#It contains at least three vowels (aeiou only),
#like aei, xazegov, or aeiouaeiouaeiou.
#It contains at least one letter that appears twice in a row,
#like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
#It does not contain the strings ab, cd, pq, or xy,
#even if they are part of one of the other requirements.

def partone():
    def threevow(word):
        count = 0
        for c in word:
            if c in 'aeiou':
                count += 1
        return(count > 2)
    def twoinrow(word):
        for i in range(len(word)-1):
            if word[i] == word[i+1]:
                return(True)
        return(False)
    def nopestrings(word):
        if 'ab' in word or 'cd' in word or 'pq' in word or 'xy' in word:
            return(True)
        else:
            return(False)
        
    nice = 0
    for w in words:
        if not(nopestrings(w)) and threevow(w) and twoinrow(w):
            nice += 1
            #print(w)
    print(nice, 'words are nice.')

#It contains a pair of any two letters that appears at least twice in the string without overlapping,
#like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
#It contains at least one letter which repeats with exactly
#one letter between them, like xyx, abcdefeghi (efe), or even aaa.
            
def parttwo():
    def twicetwice(word):
        i = 0
        while i < len(word)-1:
            j = i+2
            #testa två bokstäver (vid i) med resten av strängen (vid j)
            while j < len(word)-1:
#                print(word[i:i+2], word[j:j+2])
                if word[i:i+2] == word[j:j+2]:
#                    print(word[i:i+2], word[j:j+2])
                    return(True)
                else:
                    j += 1
            i += 2
        return(False)
        
    def onebetween(word):
        for i in range(len(word)-2):
#            print(word[i], word[i+2])
            if word[i] == word[i+2]:
                return(True)
        return(False)

    nice = 0
#    tw = 'uurcxstgmygtbstg'
#    print(onebetween(tw),twicetwice(tw))
#    exit()
    for w in words:
#        print(w, onebetween(w), twicetwice(w))
        if onebetween(w) and twicetwice(w):
            nice += 1
            print(w, nice, '------------')
    print(nice, 'words are nice.')

#167 too high
#25 fel
#65 fel
#169 fel
#1 fel
#36 fel
#41 fel

#partone()
parttwo()
