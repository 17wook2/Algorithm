## 8/49
import math
n = int(input())
cur = list(map(int, input()))
target = list(map(int, input()))
copy_cur = cur[:]
ans = math.inf
def flip(array,idx):
    for d in [-1,0,1]:
        x = idx + d
        if 0 <= x < n:
            array[x] ^= 1

def go(array,check):
    global ans
    cnt = 0
    if check:
        array[0] ^= 1
        array[1] ^= 1
        cnt += 1
    for i in range(1,n):
        if array[i-1] != target[i-1]:
            flip(array,i)
            cnt += 1
    if ''.join(list(map(str,array))) == ''.join(list(map(str,target))):
        ans = min(ans,cnt)

go(cur,0)
go(copy_cur,1)
if ans == math.inf:
    print(-1)
else:
    print(ans)