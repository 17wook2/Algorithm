import math
from itertools import combinations
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
def getScore(array):
    score = 0
    for i in range(len(array)):
        for j in range(len(array)):
            score += arr[array[i]][array[j]]
    return score

combi = list(combinations([i for i in range(n)], n//2))
ans = math.inf
for comb in combi:
    left = []
    right = []
    for i in range(n):
        if i in comb: left.append(i)
        else: right.append(i)
    l_score = getScore(left)
    r_score = getScore(right)
    ans = min(ans,abs(l_score-r_score))
print(ans)