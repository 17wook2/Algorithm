N = int(input())
arr = list(map(int,input().split()))
dp_u = [1] * N
dp_d = [1] * N
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp_u[i] = max(dp_u[i],dp_u[j]+1)
for i in range(N-1,-1,-1):
    for j in range(N-1,i,-1):
        if arr[i] > arr[j]:
            dp_d[i] = max(dp_d[i],dp_d[j]+1)
# print(dp_u)
# print(dp_d)
answer = 0
for i,j in zip(dp_d,dp_u):
    answer = max(answer,i+j)

print(answer-1)