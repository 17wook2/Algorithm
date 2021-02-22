from itertools import combinations
n,m = list(map(int,input().split()))
city = [list(map(int,input().split())) for i in range(n)]
# 하나씩 없애보면서 거리계산
bbq = []
houses = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            bbq.append((i,j))
        elif city[i][j] == 1:
            houses.append((i,j))

def cdistance(candidate):
    distance = 0
    for house in houses:
        dist = 999
        for cand in candidate:
            dist = min(dist,abs(house[0] - cand[0]) + abs(house[1] - cand[1]))
        distance += dist
    return distance

def solution():
    candidates = list(combinations(bbq,m))
    distance = 99999
    for candidate in candidates:
        distance = min(distance, cdistance(candidate))
    return distance
print(solution())



