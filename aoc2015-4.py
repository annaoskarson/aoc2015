import hashlib

data = 'yzbqklnj'

i = 1

while True:
    num = str(i)
    string = data+num
    test = hashlib.md5(string.encode())
#    h = hashlib.new(data+num)
#    test = h.hexdigest()
#    test = hash.hexdigest(data + num)
    print(string)
    print(test)
    i += 1
