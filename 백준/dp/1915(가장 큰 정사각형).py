n,m = map(int,input().split())
maps = [list(map(int,input())) for i in range(n)]
answer = 0
for i in range(1,n):
    for j in range(1,m):
        if maps[i][j] == 0:
            continue
        else:
            maps[i][j] += min(maps[i-1][j],maps[i-1][j-1],maps[i][j-1])
for row in maps:
    answer = max(answer,max(row))
print(answer*answer)