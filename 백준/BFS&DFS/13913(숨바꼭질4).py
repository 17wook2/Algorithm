from collections import deque
n,k = list(map(int,input().split()))
deq = deque([])
deq.append(n)
dp = [-1] * 100001
dp[n] = 0
char_dp = [0] * 100001
while deq:
    temp = deq.popleft()
    if temp == k:
        break
    for y in [2*temp, temp+1, temp-1]:
        if 0 <= y < 100001:
            if dp[y] == -1 or dp[y] >= dp[temp] + 1:
                dp[y] = dp[temp] + 1
                deq.append(y)
                char_dp[y] = temp
x = k
answer = [k]
while char_dp[x] != 0:
    answer.append(char_dp[x])
    x = char_dp[x]
if n == 0:
    answer.append(n)
answer.reverse()
print(dp[k])
print(*answer)