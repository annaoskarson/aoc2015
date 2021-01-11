with open('aoc2015-23-input.txt') as file:
    intext = file.read().strip().split('\n')

code = []
for line in intext:
    cmd = line.split(' ')[0]
    reg = line.split(' ',1)[1]
    code.append((cmd, reg))

def run(code, a, b):
    c = 0
    registers = {'a':a, 'b':b}
    while True:
        if len(code)-1 < c or c < 0:
            return(registers['b'])
        cmd, reg = code[c]
        if cmd == 'hlf':
            registers[reg] /= 2
            jmp = 1
        elif cmd == 'tpl':
            registers[reg] *= 3
            jmp = 1
        elif cmd == 'inc':
            registers[reg] += 1
            jmp = 1
        elif cmd == 'jmp':
            jmp = int(reg)
        elif cmd == 'jie':
            if registers[reg.split(',')[0]] % 2 == 0:
                jmp = int(reg.split(',')[1].strip())
            else:
                jmp = 1
        elif cmd == 'jio':
            if registers[reg.split(',')[0]] == 1:
                jmp = int(reg.split(',')[1].strip())
            else:
                jmp = 1
        else:
            return(registers['b'])
        c += jmp

def partone():
    return(run(code, 0, 0))

def parttwo():
    return(run(code, 1, 0))

print('Advent of Code 2015, day 23 part 1')
print(partone())
print('Advent of Code 2015, day 23 part 2')
print(parttwo())
