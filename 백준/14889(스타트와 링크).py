from itertools import combinations
import math
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

combi = list(combinations(range(n), n//2))

answer = math.inf

def getstat(members):
    num = 0
    for member in members:
        for i in range(n):
            if i in members:
                num += graph[member][i]
    return num

for comb in combi:
    ateam = getstat(comb)
    b = [i for i in range(n) if i not in comb]
    bteam = getstat(b)

    answer = min(answer,abs(ateam - bteam))

print(answer)