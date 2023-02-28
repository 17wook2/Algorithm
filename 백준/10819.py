from itertools import permutations
import math
n = int(input())
arr = list(map(int,input().split()))
combi = permutations([i for i in range(n)],n)
ans = -math.inf
for comb in combi:
    s = 0
    for i in range(n-1):
        s += abs(arr[comb[i]]-arr[comb[i+1]])
    ans = max(ans,s)
print(ans)