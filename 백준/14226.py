from collections import deque
s = int(input())
visited = [[0]*1001 for i in range(1001)]
q = deque()
q.append((1,0,0))
visited[1][0] = 1
while q:
    cnt,board,ans = q.popleft()
    if cnt == s:
        print(ans)
        break
    if not visited[cnt][cnt]:
        visited[cnt][cnt] = 1
        q.append((cnt,cnt,ans+1))
    if cnt > 0 and not visited[cnt-1][board]:
        visited[cnt-1][board] = 1
        q.append((cnt-1,board,ans+1))
    if cnt + board <= s and not visited[cnt+board][board]:
        visited[cnt+board][board] = 1
        q.append((cnt+board,board,ans+1))

