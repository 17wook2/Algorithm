import sys
input = sys.stdin.readline
m = int(input())
x = 0
for i in range(m):
    line = list(input().split())
    if len(line) == 2:
        command,idx = line
        idx = int(idx)
    else:
        command = line[0]
    if command == 'add':
        x |= (1<<idx)
    elif command == 'check':
        if x & (1<<idx) != 0:
            print(1)
        else:
            print(0)
    elif command == 'remove':
        x &= ~(1<<idx)
    elif command == 'toggle':
        x ^= (1<<idx)
    elif command == 'all':
        x = (1<<21) - 1
    elif command == 'empty':
        x = 0