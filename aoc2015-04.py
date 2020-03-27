import hashlib

data = 'yzbqklnj'
i = 1
one = False
two = False

while not (one and two):
    num = str(i)
    string = data+num
    test = hashlib.md5(string.encode())
    result = test.hexdigest()
    if result[:5] == '00000' and not one:
        print('Part one:', num)
        one = True
    if result[:6] == '000000':
        print('Part two:', num)
        two = True
    i += 1
