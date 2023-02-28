n = int(input())
t = []
p = []
dp = [0]*(n+1)
for i in range(n):
    a,b = list(map(int,input().split()))
    t.append(a)
    p.append(b)

for i in range(n):
    for j in range(i+t[i], n+1):
        dp[j] = max(dp[j],dp[i]+p[i])
print(dp[n])
