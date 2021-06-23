from itertools import combinations
n = int(input())
numbers = list(map(int,input().split()))
n_list = set()
for i in range(1,n+1):
    lst = list(combinations(numbers,i))
    for e in lst:
        n_list.add(sum(e))
# print(dp[0:10])
n_list = list(n_list)
n_list.sort()
def _print():
    for i in range(len(n_list)):
        if n_list[i] != i+1:
            return i+1
    return n_list[-1] + 1
print(_print())
