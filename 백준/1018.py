import math
n,m = map(int,input().split())
arr = []
wstart = [
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ]
bstart = [
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ]
for i in range(n):
    arr.append(input())

ans = math.inf
for i in range(n-7):
    for j in range(m-7):
        w,b = 0,0
        for k in range(8):
            for p in range(8):
                if arr[i+k][j+p] != wstart[k][p]:
                    w += 1
                if arr[i+k][j+p] != bstart[k][p]:
                    b += 1
        ans = min(ans,w,b)
print(ans)