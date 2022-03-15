from collections import deque
n,k = map(int,input().split())
state = list(map(int,input().split()))
visited = {}
ascending = ''.join(map(str,list(range(1,n+1))))
visited[''.join(map(str,state))] = 0
queue = deque([])
queue.append((state,0))
ans = -1
while queue:
    next_state,cnt = queue.popleft()
    x = ''.join(map(str,next_state))
    if x == ascending:
        ans = cnt
        break
    for i in range(n-k+1):
        copystate = next_state[:]
        for j in range(k//2):
            copystate[i+j], copystate[i+k-j-1] = copystate[i+k-j-1], copystate[i+j]
        copystate_str = ''.join(map(str,copystate))
        if copystate_str not in visited:
            visited[copystate_str] = cnt + 1
            queue.append((copystate,cnt+1))
        else:
            visited[copystate_str] = min(visited[copystate_str], cnt+1)
print(ans)