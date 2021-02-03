N = int(input())
arr = list(map(int,input().split()))
sum_array = arr[:]
dp = [1] * N
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            if sum_array[j] + arr[i] > sum_array[i]:
                sum_array[i] = sum_array[j] + arr[i]
print(max(sum_array))