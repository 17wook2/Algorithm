from itertools import combinations
n = int(input())
arr = []
for i in range(1,11):
    for combi in combinations(range(0,10),i):
        combi = sorted(combi, reverse=True)
        e = int("".join(map(str,combi)))
        arr.append(e)
arr.sort()
try:
    print(arr[n])
except:
    print(-1)