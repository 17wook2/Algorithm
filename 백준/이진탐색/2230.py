import math
n,m = list(map(int,input().split()))
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()
i = 0
j = 0
ans = math.inf
while i < n and j < n:
    tmp = abs(arr[i]-arr[j])
    if tmp < m:
        j += 1
    elif tmp > m:
        ans = min(ans,tmp)
        i += 1
    else:
        ans = m
        break

print(ans)