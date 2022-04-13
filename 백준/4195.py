import sys
input = sys.stdin.readline
def find(x):
    if parent[x] == x:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return p
def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
        cnt[a] += cnt[b]
t = int(input())
for _ in range(t):
    n = int(input())
    parent = {}
    cnt = {}
    for i in range(n):
        l,r = input().split()
        if l not in parent:
            parent[l] = l
            cnt[l] = 1
        if r not in parent:
            parent[r] = r
            cnt[r] = 1
        union(l,r)
        print(cnt[find(l)])
