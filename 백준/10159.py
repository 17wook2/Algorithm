from collections import deque
n = int(input())
m = int(input())
arr = [[0]*(n+1) for i in range(n+1)]
for i in range(m):
    a,b = list(map(int,input().split()))
    arr[a][b] = 1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if arr[i][k] and arr[k][j]: arr[i][j] = 1

for i in range(1,n+1):
    cnt = 0
    for j in range(1,n+1):
        if not arr[i][j] and not arr[j][i]: cnt += 1
    print(cnt-1)