from itertools import permutations
n,k = list(map(int,input().split()))
arr = list(map(int,input().split()))
pers = list(permutations([i for i in range(n)], n))
cnt = 0
for per in pers:
    x = 0
    for p in per:
        x += arr[p]
        x -= k
        if x < 0: break
    if x >= 0: cnt += 1
print(cnt)

