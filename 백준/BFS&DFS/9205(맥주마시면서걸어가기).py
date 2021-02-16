from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    x,y = list(map(int,input().split()))
    store = []
    for i in range(n):
        store.append(list(map(int,input().split())))
    target_x , target_y = list(map(int,input().split()))
    stack = [(x,y)]
    visited = [0] * (len(store) + 1)
    str1 = 'sad'
    while stack:
        # print(stack)
        a,b = stack.pop()
        if abs(a-target_x) + abs(b-target_y) <= 1000:
            str1 = 'happy'
            break
        for k in range(len(store)):
            if not visited[k] and abs(a-store[k][0]) + abs(b-store[k][1]) <= 1000:
                stack.append((store[k][0],store[k][1]))
                visited[k] = 1
    print(str1)

