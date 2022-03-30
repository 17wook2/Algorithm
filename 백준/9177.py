from collections import deque
n = int(input())
for i in range(n):
    a,b,c = list(input().split())
    la = len(a)
    lb = len(b)
    lc = len(c)
    queue = deque([])
    queue.append((0,0))
    visited = [[0]*210 for i in range(210)]
    ans = 0
    d = ['no','yes']
    while queue:
        x,y = queue.popleft()
        visited[x][y] = 1
        if x == la and y == lb:
            ans = 1
            break
        cnt = x + y
        if x < la:
            if c[cnt] == a[x] and not visited[x+1][y]:
                queue.append((x+1,y))
                visited[x+1][y] = 1
        if y < lb:
            if c[cnt] == b[y] and not visited[x][y+1]:
                queue.append((x,y+1))
                visited[x][y+1] = 1
    print(f"Data set {i+1}: {d[ans]}")
