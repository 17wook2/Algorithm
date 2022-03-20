from collections import deque
n,k = map(int,input().split())
length = len(list(str(n)))
queue = deque([])
queue.append((str(n),0))
ans = 0
while queue:
    visited = {}
    for _ in range(len(queue)):
        x,cnt = queue.popleft()
        if cnt == k:
            ans = max(ans,int(x))
            continue
        for i in range(length-1):
            for j in range(i+1,length):
                tolist = list(x)
                if i == 0 and tolist[j] == '0':
                    continue
                tolist[i],tolist[j] = tolist[j],tolist[i]
                tostr = ''.join(tolist)
                if tostr not in visited:
                    visited[tostr] = 1
                    queue.append((tostr, cnt+1))

if n < 10 or (length == 2 and n%10 == 0):
    print(-1)
else:
    print(ans)
