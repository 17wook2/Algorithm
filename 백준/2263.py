import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n = int(input())
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))
idx = [0]*(n+1)
for i in range(n):
    idx[inorder[i]] = i
ans = []
def func(ileft,iright,pleft,pright):
    if ileft > iright or pleft > pright:
        return
    root = postorder[pright]
    ans.append(root)
    lshift = idx[root] - ileft
    rshift = iright - idx[root]
    func(ileft,ileft+lshift-1,pleft,pleft+lshift-1)
    func(iright-rshift+1,iright,pright-rshift,pright-1)
func(0,n-1,0,n-1)
print(*ans)
