n = int(input())
arr = []
for i in range(n):
    t = list(map(int,input().split()))
    arr.append(t)

# 종료시간이 빠른순으로 정렬
arr.sort(key = lambda x:(x[1],x[0]))
ans = 0
t = 0
for i in range(n):
    if arr[i][0] >= t:
        ans += 1
        t = arr[i][1]
    else:
        continue

print(ans)
