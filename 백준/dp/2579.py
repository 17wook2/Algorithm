n = int(input())
lst = [0]
dp = [0] * (n+1)
for i in range(n):
    lst.append(int(input()))
dp[1] = lst[1]
try:
    dp[2] = lst[1] + lst[2]
except IndexError:
    pass
for i in range(3,n+1):
    dp[i] = max(dp[i-3]+lst[i-1]+lst[i],dp[i-2]+lst[i])
print(dp[n])