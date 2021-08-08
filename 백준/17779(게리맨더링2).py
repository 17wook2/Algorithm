import math
def solve(x,y,d1,d2):
    temp = [[0 for i in range(n+1)] for i in range(n+1)]
    for i in range(d1+1):
        temp[x+i][y-i] = 5
        temp[x+d2+i][y+d2-i] = 5

    for i in range(d2+1):
        temp[x+i][y+i] = 5
        temp[x+d1+i][y-d1+i] = 5

    for i in range(x+1,x+d1+d2):
        cnt = 0
        f = False
        for j in range(1,n+1):
            if cnt == 2:
                break
            if temp[i][j] == 5:
                f = True
                cnt += 1
            if f:
                temp[i][j] = 5

    for i in range(1,n+1):
        for j in range(1,n+1):
            if temp[i][j] == 5:
                continue
            if 1 <= i < x + d1 and 1 <= j <= y:
                temp[i][j] = 1
            if 1 <= i <= x + d2 and y < j <= n:
                temp[i][j] = 2
            if x + d1 <= i <= n and 1 <= j < y - d1 + d2:
                temp[i][j] = 3
            if x+ d2 < i <= n and y - d1 + d2 <= j <= n:
                temp[i][j] = 4

    population = [[],[],[],[],[]]
    for i in range(1,n+1):
        for j in range(1,n+1):
            population[temp[i][j]-1].append(a[i-1][j-1])

    sp = list(map(sum, population))
    return max(sp) - min(sp)

result = math.inf
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
for x in range(1,n+1):
    for y in range(1,n+1):
        for d1 in range(1,n+1):
            for d2 in range(1,n+1):
                if 1 <= x < x + d1 + d2 <= n and 1 <= y - d1 < y < y + d2 <= n:
                    result =  min(result,solve(x,y,d1,d2))

print(result)
