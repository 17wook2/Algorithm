import math
import bisect
n = int(input())
arr = list(map(int,input().split()))
dp = [0]*n
tmp = [-math.inf]
for i in range(n):
    if tmp[-1] < arr[i]:
        tmp.append(arr[i])
        dp[i] = len(tmp) - 1
    else:
        idx = bisect.bisect_left(tmp,arr[i])
        dp[i] = idx
        tmp[idx] = arr[i]
k = max(dp)
print(k)
ans = []
for i in range(n-1,-1,-1):
    if dp[i] == k:
        ans.append(arr[i])
        k -= 1
print(*ans[::-1])

