import heapq
import math
import sys
input = sys.stdin.readline
n = int(input())
arr = []
heap = []
for i in range(n):
    arr.append(list(map(float,input().split())))
parent = [-1]*(n+1)
ans = 0
def get_distance(a,b):
    x = abs(a[0]-b[0])**2
    y = abs(a[1]-b[1])**2
    return math.sqrt(x+y)
def find(x):
    if parent[x] < 0:
        return x
    parent[x] = find(parent[x])
    return parent[x]
def union(u,v):
    if u < v:
        parent[u] += parent[v]
        parent[v] = u
    else:
        parent[v] += parent[u]
        parent[u] = v
for i in range(n):
    for j in range(i+1,n):
        distance = get_distance(arr[i],arr[j])
        heapq.heappush(heap,(distance,i,j))
while heap:
    d,x,y = heapq.heappop(heap)
    x = find(x)
    y = find(y)
    if x != y:
        union(x,y)
        ans += d

print(ans)