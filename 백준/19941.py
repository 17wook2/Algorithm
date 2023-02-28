n,k = map(int,input().split())
row = list(input())
visited = [0]*n
cnt = 0
for i in range(n):
    if row[i] == 'H':
        for j in range(i-k,i+k+1):
            if j < 0 or j >= n: continue
            if row[j] == 'H': continue
            if row[j] == 'P' and not visited[j]:
                cnt += 1
                visited[j] = 1
                break
print(cnt)
