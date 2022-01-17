from itertools import permutations
n,s = list(map(int,input().split()))
arr = list(map(int,input().split()))
cnt = 0
visited = [0]*n
def func(d,k):
    global cnt
    if k == n:
        if d == s:
            cnt += 1
        return
    func(d,k+1)
    func(d+arr[k],k+1)


func(0,0)
if s == 0:
    cnt-=1
print(cnt)
