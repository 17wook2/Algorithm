first = input()
second = input()
lcs = []
dp = [[""]*(len(first) + 1) for i in range(len(second) + 1)]
for i in range(len(second)):
    for j in range(len(first)):
        if second[i] == first[j]:
            dp[i+1][j+1] = dp[i][j] + second[i]
        else:
            dp[i+1][j+1] = dp[i][j+1] if len(dp[i][j+1]) > len(dp[i+1][j]) else dp[i+1][j]
# print(dp)
print(len(dp[len(second)][len(first)]))
print(dp[len(second)][len(first)])