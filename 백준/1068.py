n = int(input())
parent = list(map(int,input().split()))
k = int(input())
child = [[] for i in range(n)]
for i in range(n):
    if parent[i] != -1:
        child[parent[i]].append(i)
if parent[k] != -1:
    child[parent[k]].remove(k)
parent[k] = -2
def find(node):
    if parent[node] == -1:
        return True
    elif parent[node] == -2:
        return False
    else:
        return find(parent[node])
ans = 0
for i in range(n):
    if find(i) and len(child[i]) == 0:
        ans += 1
print(ans)
