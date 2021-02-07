#unsolved
def find_left(array,target): # 이분탐색으로 원하는 부분 이분탐색
    start = 0
    end = len(array) - 1
    ans = 0
    while start <= end:
        # print(start,end)
        mid = (start + end) // 2
        if array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start
# print(find_left([0,10],5))

n = int(input())
arr = list(map(int,input().split()))
dp = [0]
for i in range(len(arr)):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    elif arr[i] < dp[-1]:
        dp[find_left(dp,arr[i])] = arr[i]
print(len(dp)-1)
# dp = [1] * n
# for i in range(n): # O(n^2)
#     for j in range(i):
#        if arr[i] > arr[j]:
#            dp[i] = max(dp[i],dp[j]+1)
# print(max(dp))

