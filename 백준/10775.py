g = int(input())
p = int(input())
parent = [i for i in range(100001)]
ans = p
def find(x):
    if parent[x] == x:
        return x
    p = find(parent[x])
    parent[x] = p
    return p
def union(u,v):
    u = find(u)
    v = find(v)
    if u < v:
        parent[v] = u
    else:
        parent[u] = v
for i in range(p):
    x = int(input())
    px = find(x)
    if px == 0:
        ans = i
        break
    union(px,px-1)

print(ans)