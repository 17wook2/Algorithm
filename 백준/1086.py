import sys
from math import factorial, gcd
input = sys.stdin.readline
def go(mod,bit):
    if bit == (1<<n) -1:
        if mod == 0: return 1
        else: return 0
    if dp[mod][bit] != -1: return dp[mod][bit]
    res = 0
    for i in range(n):
        if not bit & (1<<i):
            new_mod = ((mod * md[arr_len[i]]) % k + arr[i]) % k
            res += go(new_mod,bit | 1 << i)
    dp[mod][bit] = res
    return dp[mod][bit]

n = int(input())
arr = [int(input()) for i in range(n)]
k = int(input())
arr_len = [len(str(x)) for x in arr]
arr = [i % k for i in arr]
md = [1]
for i in range(50): md.append((md[-1]*10) % k)
dp = [[-1]*(1<<n) for i in range(k)]
ans = go(0,0)
if ans == 0:
    print('0/1')
else:
    f = factorial(n)
    if ans == f or k == 1:
        print('1/1')
    else:
        gcd = gcd(ans,f)
        print(f'{ans//gcd}/{f//gcd}')



