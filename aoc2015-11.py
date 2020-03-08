
passwd = 'hepxcrrq'
passwd = 'hepxxyzz'


def partone(passwd):
    def incr(word):
        w = list(word)
        c = 1
        while c < len(w)+1:
#            print(w[-c])
            if w[-c] == 'z':
                w[-c] = 'a'
                c += 1
            else:
                w[-c] = chr(ord(w[-c])+1)
                if w[-c] == 'i':
                    w[-c] = 'j'
                elif w[-c] == 'o':
                    w[-c] = 'p'
                elif w[-c] == 'l':
                    w[-c] = 'm'
                word = ''.join(w)
                return(word)

    def incstrait(word):
        c = 0
        while c < len(word)-2:
            w = list(word)
            if ord(w[c]) == ord(w[c+1])-1 and ord(w[c]) == ord(w[c+2])-2:
#                print(w[c], ord(w[c]), ord(w[c+1]), ord(w[c+2]))
                return(True)
            else:
                c += 1
        return(False)

    def notiol(word):
        return(not('i' in word or 'o' in word or 'l' in word))

    def twopairs(word):
        i = 0
        while i < len(word)-3:
            j = i+2
            if word[i] == word[i+1]:
                while j < len(word)-1:
                    if word[j] == word[j+1]:
                        return(True)
                    else:
                        j += 1
            i += 1
        return(False)

#    print('hijklmmn', incstrait('hijklmmn'), notiol('hijklmmn'), twopairs('hijklmmn'))
#    print('abbceffg', incstrait('abbceffg'), notiol('abbceffg'), twopairs('abbceffg'))
#    print('abbcegjk', incstrait('abbcegjk'), notiol('abbcegjk'), twopairs('abbcegjk'))
#    print('hijklmmn', incstrait('hijklmmn'), notiol('hijklmmn'), twopairs('hijklmmn'))

#    passwd = 'abcdefgh' #abcdffaa
#    passwd = 'ghijklmn' #ghjaabcc
    
    found = False
    while not found:
        nextp = incr(passwd)
#        print(nextp)
        if incstrait(nextp) and notiol(nextp) and twopairs(nextp):
            print(nextp)
            found = True
        passwd = nextp


partone(passwd)
#parttwo()

#hepxepqr fel
