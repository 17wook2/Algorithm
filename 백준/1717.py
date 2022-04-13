import sys
input = sys.stdin.readline
n,m = map(int,input().split())
parent = [-1]*(n+1)
def union(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if parent[a] < parent[b]:
        parent[a] += parent[b]
        parent[b] = a
    else:
        parent[b] += parent[a]
        parent[a] = b
def find(node):
    if parent[node] < 0:
        return node
    else:
        p = find(parent[node])
        parent[node] = p
        return p
def check(a,b):
    if find(a) == find(b):
        return True
    else:
        return False
for _ in range(m):
    x,a,b = list(map(int,input().split()))
    if a > b: a,b = b,a
    if x == 0:
        union(a,b)
    else:
        if check(a,b):
            print("YES")
        else:
            print("NO")
