with open('aoc2015-6-input.txt') as file:
    cmds = file.readlines()

cmds = [line.strip() for line in cmds]
#cmds = ['turn on 0,0 through 999,999']

#print(cmds[0])
#exit()

def partone():
    bulbs = [ [ 0 for i in range(1000) ] for j in range(1000) ]
#    print(len(bulbs), len(bulbs[0]))
#    exit()

    def lighted(b):
        many = 0
        for a in range(1000):
            many = many + b[a].count(1)
            #print(b[a].count(1))
        return(many)

    def act(c,do):
        ax = int(c[0].split(',')[0])
        ay = int(c[0].split(',')[1])
        bx = int(c[2].split(',')[0])
        by = int(c[2].split(',')[1])
        #fixa alla inom rektangeln.
        for y in range(ay,by+1):
            for x in range(ax,bx+1):
                if do == 'on':
                    bulbs[y][x] = 1
                elif do == 'off':
                    bulbs[y][x] = 0
                elif do == 'tog':
                    if bulbs[y][x] == 0:
                        bulbs[y][x] = 1
                    elif bulbs[y][x] == 1:
                        bulbs[y][x] = 0
                
    for cmd in cmds:
        cmd = cmd.split(' ')
        if cmd[:2] == ['turn', 'on']:
            act(cmd[2:], 'on')
        elif cmd[:2] == ['turn', 'off']:
            act(cmd[2:], 'off')
        elif cmd[:1] == ['toggle']:
            act(cmd[1:], 'tog')
    print(lighted(bulbs))

def parttwo():
    bulbs = [ [ 0 for i in range(1000) ] for j in range(1000) ]
#    print(len(bulbs), len(bulbs[0]))
#    exit()

    def lighted(b):
        w = 0
        for a in range(1000):
            w = w + sum(b[a])
            #print(b[a].count(1))
        return(w)

    def act(c,do):
        ax = int(c[0].split(',')[0])
        ay = int(c[0].split(',')[1])
        bx = int(c[2].split(',')[0])
        by = int(c[2].split(',')[1])
        #fixa alla inom rektangeln.
        for y in range(ay,by+1):
            for x in range(ax,bx+1):
                if do == 'on':
                    bulbs[y][x] += 1
                elif do == 'off':
                    if bulbs[y][x] > 0:
                        bulbs[y][x] += -1
                elif do == 'tog':
                    bulbs[y][x] += 2
                
    for cmd in cmds:
        cmd = cmd.split(' ')
        if cmd[:2] == ['turn', 'on']:
            act(cmd[2:], 'on')
        elif cmd[:2] == ['turn', 'off']:
            act(cmd[2:], 'off')
        elif cmd[:1] == ['toggle']:
            act(cmd[1:], 'tog')
    print(lighted(bulbs))


#partone()
parttwo()
