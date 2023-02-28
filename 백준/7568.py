n = int(input())
arr = []
for i in range(n):
    x,y = map(int,input().split())
    arr.append((i,x,y))
rank = [0]*n
for i in range(n):
    idx,x,y = arr[i]
    cnt = 1
    for j in range(n):
        if i == j: continue
        if x < arr[j][1] and y < arr[j][2]:
            cnt += 1
    rank[idx] = cnt
print(*rank)