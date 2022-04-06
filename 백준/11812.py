import sys
input = sys.stdin.readline
n,k,q = list(map(int,input().split()))
def getparent(node):
    t = node // k
    if node % k == 0:
        t -= 1
    return t
def getheight(node):
    depth = 0
    if k == 1:
        depth = node
    else:
        if node != 0:
            depth = 1
            left = 1; right = k;
            while not left <= node <= right:
                depth += 1
                left = left * k + 1
                right = right * k + k
    return depth
for _ in range(q):
    x,y = map(int,input().split())
    if x > y: x,y = y,x
    x-= 1; y-=1;
    ans = 0
    gx = getheight(x)
    gy = getheight(y)
    ans += gy - gx
    if k == 1:
        print(ans)
        continue
    for i in range(gy-gx):
        y = getparent(y)
    while x != y:
        x = getparent(x)
        y = getparent(y)
        ans += 2
    print(ans)