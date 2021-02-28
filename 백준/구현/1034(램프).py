n,m = map(int,input().split())
array = []
for i in range(n):
    array.append(list(map(int,input())))
k = int(input())
dp = [0] * (n)
if k % 2 == 0:
    for i in range(n):
        zero = array[i].count(0)
        if zero % 2 == 0 and zero <= k:
            for j in range(n):
                if array[i] == array[j]:
                    dp[i] += 1
else:
    for i in range(n):
        zero = array[i].count(0)
        if zero % 2 == 1 and zero <= k:
            for j in range(n):
                if array[i] == array[j]:
                    dp[i] += 1
print(max(dp))