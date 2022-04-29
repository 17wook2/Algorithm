import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n,r,q = list(map(int,input().split()))
def count(x):
    size[x] = 1
    for node in tree[x]:
        if not size[node]: ## 방문 안했다면
            count(node)
            size[x] += size[node]
size = [0]*(n+1)
tree = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
count(r)
for i in range(q):
    print(size[int(input())])