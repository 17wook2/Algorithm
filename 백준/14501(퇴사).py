n = int(input())
t = []
p = []
for i in range(n):
    a,b = list(map(int,input().split()))
    t.append(a)
    p.append(b)
dp = [0 for i in range(n)]
dp.append(0)

for i in range(n-1,-1,-1):
    if i + t[i] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], p[i] + dp[i+t[i]])

print(dp[0])