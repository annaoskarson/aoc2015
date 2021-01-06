number = 36000000

def presents(house):
    import sympy
    return(sum([elf*10 for elf in sympy.divisors(house)]))

def partone():
    n = 0
    h = 0
    while n < number:
        h += 1
        n = presents(h)
    return(h)

def presents2(house):
    import sympy
    return(sum([elf*11 for elf in sympy.divisors(house) if house // elf <= 50]))

def parttwo():
    n = 0
    h = 0
    while n < number:
        h += 1
        n = presents2(h)
    return(h)

print('Advent of Code 2015, day 20 part 1')
print(partone())
print('Advent of Code 2015, day 20 part 2')
print(parttwo())
