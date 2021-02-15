from collections import deque
n,k = list(map(int,input().split()))
deq = deque([])
deq.append(n)
answer = 0
dp = [-1] * 100001
dp[n] = 0
while deq:
    temp = deq.popleft()
    print(temp)
    # print(temp)
    if temp == k:
        break
    if 0 <= temp * 2 < 100001:
        if dp[temp*2] == -1 or dp[temp*2] >= dp[temp]:
                dp[temp*2] = dp[temp]
                deq.append(temp*2)
    for y in [temp+1,temp-1]:
        if 0 <= y < 100001:
            if dp[y] == -1 or dp[y] >= dp[temp] + 1:
                dp[y] = dp[temp] + 1
                deq.append(y)
# print(dp)
print(dp[k])

