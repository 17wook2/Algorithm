from collections import deque
N = int(input())
net = int(input())
connected = []
for i in range(net):
    lst = list(map(int,input().split()))
    connected.append(lst)
# network = [[1 if i==j else 0 for j in range(N)] for i in range(N)]
network = [[0]*N for i in range(N)]
for connection in connected:
    x,y = connection[0],connection[1]
    network[x-1][y-1] = 1
    network[y-1][x-1] = 1
answer = 0
def bfs(start):
    global answer
    deq = deque([])
    visited = [0]*N
    deq.append(start)
    visited[start] = 1
    while deq:
        # print(deq)
        temp = deq.popleft()
        visited[temp] = 1
        for i,v in enumerate(network[temp]):
            if visited[i] == 0 and v == 1 and temp != i:
                deq.append(i)
                visited[i] = 1
                answer += 1
    # print(visited)
bfs(0)
print(answer)