import hashlib

data = 'yzbqklnj'
i = 1

while not 'six' in locals():
    num = str(i)
    string = data+num
    result = hashlib.md5(string.encode()).hexdigest()
    if result[:6] == '000000' and not 'six' in locals():
        six = num
    if result[:5] == '00000' and not 'five' in locals():
        five = num
    i += 1

print('Advent of Code 2015, day 2 part 1')
print(five)
print('Advent of Code 2015, day 2 part 2')
print(six)
