import math
v,e = map(int,input().split())
distance = [[math.inf]*400 for i in range(400)]
for _ in range(e):
    a,b,c = list(map(int,input().split()))
    distance[a-1][b-1] = c
for k in range(v):
    for i in range(v):
        for j in range(v):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
ans = math.inf
for i in range(v):
    for j in range(v):
        if distance[i][j] != math.inf and distance[j][i] != math.inf:
            ans = min(ans,distance[i][j] + distance[j][i])
print(ans) if ans != math.inf else print(-1)

