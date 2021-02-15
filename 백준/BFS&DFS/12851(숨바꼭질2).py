import math
from collections import deque
n,k = list(map(int,input().split()))
deq = deque([])
deq.append(n)
count = 0
dp = [-1] * 100001 # k까지 가는데 최단시간
dp[n] = 0
while deq:
    x = deq.popleft()
    if x == k:
        count += 1
    for y in [x*2,x+1,x-1]:
        if 0<= y < 100001:
            if dp[y] == -1 or dp[y] >= dp[x]+1:
                dp[y] = dp[x] + 1
                deq.append(y)
# print(dp[0:k])
print(dp[k])
print(count)



