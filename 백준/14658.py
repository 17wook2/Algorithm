import sys
input = sys.stdin.readline
n,m,l,k = list(map(int,input().split()))
stars = []
for i in range(k):
    x,y = list(map(int,input().split()))
    stars.append((x,y))
ans = -1
for i in range(len(stars)):
    for j in range(len(stars)):
        x = stars[i][0]
        y = stars[j][1]
        cnt = 0
        for k in range(len(stars)):
            nx = stars[k][0]
            ny = stars[k][1]
            if x <= nx <= x + l and y <= ny <= y + l:
                cnt += 1
        ans = max(ans,cnt)

print(len(stars) - ans)