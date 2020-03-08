phrase = '1113122113'

#phrase = '111221'
#phrase = '1211'
#phrase = '21'


def partone(num):
    def talk(number):
        new = ''
        count = 1
        for i in range(len(number)):
            if i == len(number)-1:
                new = new + str(count) + str(number[i])
                count = 1
            elif number[i] == number[i+1]:
                count += 1
            else:
                new = new + str(count) + str(number[i])
                count = 1
        return(new)

    i = 0
    while i < 50:
        nnum = talk(num)
        i += 1
        num = nnum
        print(i, len(num))
        if i == 40:
            print('After 40 times', len(num))
        elif i == 50:
            print('After 50 times', len(num))


def parttwo(num):
    def talk(number):
        new = ''
        count = 1
        for i in range(len(number)):
            if i == len(number)-1:
                new = new + str(count) + str(number[i])
                count = 1
            elif number[i] == number[i+1]:
                count += 1
            else:
                new = new + str(count) + str(number[i])
                count = 1
        return(new)

    length = 0
    i = 0
    comp = ''
    while i < 50:
        print(i, len(comp), len(num), length)
        nnum = talk(num)
        i += 1
        if i % 4 == 0: #i % 4 == 0:
            #jämför comp med nnum bakifrån och ta bort alla som är samma
            c = 1
            while True: #c < len(comp):
                if comp[-1:] == nnum[-1:]:
                    nnum = nnum[:-1]
                    comp = comp[:-1]
                    c += 1
                else:
                    break
            length = length + c
            comp = nnum
        if i == 40:
            print('After 40 times', length+len(nnum), 360154)
        num = nnum
    length = length + len(num)
    print('After 50 times', length)

partone(phrase)
#parttwo(phrase)
# 1826086 too low

# Rätt   : 360154
# 40 (1) : 163444 (89)
# 40 (2) : 287978 (56)
# 40 (4) : 337665 (45)
