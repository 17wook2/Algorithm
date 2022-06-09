from itertools import permutations
n = int(input())
arr = list(map(int,input().split()))
ans = 0
def func(array):
    x = 0
    for i in range(n-1):
        x += abs(array[i] - array[i+1])
    return x

for i in permutations(arr, n):
    tmp = func(i)
    ans = max(ans,tmp)
print(ans)
