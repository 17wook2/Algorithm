n = int(input())
arr = list(map(int,input().split()))
dp = [1]*n
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i],dp[j]+1)
k = max(dp)
print(k)
start = dp.index(k)
p = arr[start]
cnt = 0
ans = [p]
for i in range(start-1,-1,-1):
    if dp[i] + 1 == k:
        ans.append(arr[i])
        k = dp[i]
print(*ans[::-1])