#unsolved
N = int(input())
w = [0]
for i in range(N):
    w.append(int(input()))
dp = [0]
dp.append(w[1])
if N>1:
    dp.append(w[1]+w[2])
for i in range(3,N+1):
    dp.append(max(dp[i-1], dp[i-2] + w[i], dp[i-3] + w[i-1] + w[i]))
print(dp[N])