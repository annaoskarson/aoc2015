phrase = '1113122113'

#phrase = '111221'
#phrase = '1211'
#phrase = '21'


def first(num):
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
        print(i)
        if i == 40:
            print('Part one: After 40 times', len(num))
        elif i == 50:
            print('Part one: After 50 times', len(num))


def second(num):
#I think this one never got correct ...
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
#        print(i, len(comp), len(num), length)
        nnum = talk(num)
        i += 1
        if i % 4 == 0:
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
            print('Part one: After 40 times', length+len(nnum), 360154)
        num = nnum
    length = length + len(num)
    print('Part two: After 50 times', length)

first(phrase)
second(phrase)
