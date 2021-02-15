from collections import deque
a,b = list(map(int,input().split()))
queue = deque([])
dp = [-1]*100001
dp[a] = 0
queue.append(a)
while queue:
    temp = queue.popleft()
    if temp == b:
        break
    for y in [temp*2,temp+1,temp-1]:
        if 0<= y < 100001:
            if dp[y] == -1 or dp[y] >= dp[temp] + 1:
                dp[y] = dp[temp] + 1
                queue.append(y)
print(dp[b])
