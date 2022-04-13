n = int(input())
arr = []
_max = 0
for i in range(n):
    tmp = list(map(int,input().split()))
    _max = max(_max,tmp[1])
    arr.append(tmp)
start = 1
end = _max
ans = 0
def psum(mid):
    cnt = 0
    for q in arr:
        a,c,b = q
        cnt += max(0, (min(mid,c)-a)//b +1)
    return cnt

while start < end:
    mid = (start+end) // 2
    cnt = psum(mid)
    if cnt % 2 == 0:
        start = mid + 1
    else:
        end = mid
if psum(start) % 2 == 1:
    cnt = psum(start) - psum(start - 1)
    print(start, cnt)
else:
    print("NOTHING")

