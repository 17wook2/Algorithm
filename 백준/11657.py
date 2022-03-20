import sys
import math
input = sys.stdin.readline
n,m = map(int,input().split())
routes = []
for i in range(m):
    a,b,c = list(map(int,input().split()))
    routes.append((a-1,b-1,c))
distance = [math.inf]*n
distance[0] = 0
def bellman():
    for i in range(n):
        for route in routes:
            a,b,c = route
            if distance[a] != math.inf and distance[b] > distance[a] + c:
                distance[b] = distance[a] + c
                if i == n-1:
                    return -1
if bellman() == -1:
    print(-1)
else:
    for i in range(1,n):
        if distance[i] == math.inf:
            print(-1)
        else:
            print(distance[i])





