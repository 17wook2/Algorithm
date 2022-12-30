import sys
input = sys.stdin.readline
def act(command):
    global pointer, code_idx, data_idx, cnt, sp
    if command == '-':
        arr[pointer] -= 1
        if arr[pointer] == -1:
            arr[pointer] = 255
    elif command == '+':
        arr[pointer] += 1
        if arr[pointer] == 256:
            arr[pointer] = 0
    elif command == '<':
        pointer -= 1
        if pointer == -1:
            pointer = m-1
    elif command == '>':
        pointer += 1
        if pointer == m:
            pointer = 0
    elif command == '[':
        if arr[pointer] == 0:
            code_idx = move[code_idx]
        else:
            loop_stack[sp] = cnt
            stack[sp] = code_idx
            sp += 1
    elif command == ']':
        if arr[pointer] != 0:
            code_idx = move[code_idx]
            loop_stack[sp-1] = cnt
        else:
            sp -= 1
    elif command == '.':
        pass
    elif command == ',':
        if data_idx < i:
            arr[pointer] = ord(data[data_idx])
            data_idx += 1
        else:
            arr[pointer] = 255
    code_idx += 1

def go():
    global cnt
    global code_idx, loop_idx
    for _ in range(50000000):
        if code_idx >= c:
            print("Terminates")
            return
        act(commands[code_idx])
        cnt += 1
    for _ in range(50000000):
        act(commands[code_idx])
        cnt += 1
    for x in range(sp):
        if cnt-1-loop_stack[x] <= 50000000:
            print(f"Loops {stack[i]} {move[stack[i]]}")
            break
tc = int(input())
for _ in range(tc):
    m,c,i = list(map(int,input().split()))
    commands = input()
    arr = [0]*m
    pointer = 0; code_idx = 0; data_idx = 0; loop_idx = float('inf')
    data = input()
    move = [0]*c
    stack = [0]*c
    loop_stack = [0]*c
    sp = 0
    cnt = 0
    for idx,command in enumerate(commands):
        if command == '[':
            sp += 1
            stack[sp] = idx
        elif command == ']':
            move[stack[sp]] = idx
            move[idx] = stack[sp]
            sp -= 1
    go()