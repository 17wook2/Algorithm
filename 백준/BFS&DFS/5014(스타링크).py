from collections import deque
f,s,g,u,d = list(map(int,input().split()))
dp = [-1] * (f+1)
dp[s] = 0
queue = deque([s])
while queue:
    temp = queue.popleft()
    if temp == g:
        break
    for y in [temp + u, temp - d]:
        if 1 <= y <= f:
            if dp[y] == -1:
                dp[y] = dp[temp] + 1
                queue.append(y)
print(dp[g] if dp[g] != -1 else 'use the stairs')
