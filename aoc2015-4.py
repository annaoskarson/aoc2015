import hashlib

data = 'yzbqklnj'
i = 1


while True:
    num = str(i)
    string = data+num
    test = hashlib.md5(string.encode())
    result = test.hexdigest()
    if result[:5] == '00000':
        print('Answer A:', num)
    if result[:6] == '000000':
        print('Answer B:', num)
    i += 1
