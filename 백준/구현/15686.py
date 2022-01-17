from itertools import combinations
n,m = list(map(int,input().split()))
city = []
for i in range(n):
    tmp = list(map(int,input().split()))
    city.append(tmp)

chicken = []
house = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chicken.append((i,j))
        if city[i][j] == 1:
            house.append((i,j))

combi = list(combinations(chicken,m))
answer = 9999999
for comb in combi:
    cd = 0
    for h in house:
        d = 1000
        for chick in comb:
            a,b = h
            x,y = chick
            d = min(d,abs(a-x)+abs(b-y))
        cd += d
    answer = min(answer,cd)

print(answer)



