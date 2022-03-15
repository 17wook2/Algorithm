n = int(input())
crain = list(map(int,input().split()))
m = int(input())
boxes = list(map(int,input().split()))
crain.sort(reverse=True)
boxes.sort(reverse=True)
box_idx = 0
ans = 0
visited = [0]*m
pos = [0]*n
if max(crain) < max(boxes):
    print(-1)
else:
    while box_idx != m:
        for i in range(n):
            while pos[i] < m:
                if not visited[pos[i]] and crain[i] >= boxes[pos[i]]:
                    visited[pos[i]] = 1
                    pos[i] += 1
                    box_idx += 1
                    break
                pos[i] += 1
        ans += 1
    print(ans)


