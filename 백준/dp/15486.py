import sys
n = int(sys.stdin.readline())
time = [0]
pay = [0]
dp = [0] * (n+3)
for _ in range(n):
    lst = list(map(int,sys.stdin.readline().split()))
    time.append(lst[0])
    pay.append(lst[1])
for i in range(1,n+1): # i일
    if i + time[i] <= n+1:
        dp[i+time[i]] = max(dp[i]+pay[i], dp[i+time[i]])
    dp[i+1] = max(dp[i+1],dp[i])
print(dp)

