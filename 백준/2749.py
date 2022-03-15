n = int(input())
cycle = 1500000
m = 1000000
dp = [0]*cycle
dp[0] = 0
dp[1] = 1
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    for i in range(2,cycle):
        dp[i] = (dp[i-1] + dp[i-2]) % m
    print(dp[n%cycle])


