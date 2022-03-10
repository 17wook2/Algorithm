import math
n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(map(int,input())))
ans = -1
for i in range(n):
    for j in range(m):
        for k in range(-n,n):
            for p in range(-m,m):
                x,y = i,j
                start = ''
                if k == 0 and p == 0:
                    continue
                while 0 <= x < n and 0 <= y < m:
                    start += str(arr[x][y])
                    t = int(start)
                    root_t = math.sqrt(t)
                    if root_t.is_integer():
                        ans = max(ans, t)
                    x = x + k
                    y = y + p
print(ans)
