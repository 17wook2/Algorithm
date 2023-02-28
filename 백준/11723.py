m = int(input())
s = 0
for i in range(m):
    command = list(input().split())
    if len(command) == 2:
        order, num = command
        num = int(num)
        if order == 'add':
            s |= (1<<num)
        elif order == 'remove':
            s &= ~(1<<num)
        elif order == 'check':
            if s & (1<<num) == 1: print(1)
            else: print(0)
        elif order == 'toggle':
            s ^= (1<<num)
    else:
        if command == 'all':
            s = (1<<21) -1
        elif command == 'empty':
            s = 0

