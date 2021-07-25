import copy
n,m,h = list(map(int,input().split()))
graph = [[0 for i in range(n+1)] for i in range(h+1)]
for i in range(m):
    a,b = list(map(int,input().split()))
    graph[a][b] = 1
    graph[a][b+1] = 1

def checkpoint(graph):
    point = []
    for i in range(1, h+1):
        for j in range(1, n):
            if graph[i][j] == 0 and graph[i][j + 1] == 0:
                point.append((i, j))
    return point

def checkresult(graph):
    for i in range(1,n+1): ## 1번줄부터 n번줄까지
        start = i
        for j in range(1,h+1):
            if graph[j][start] == 1: ## 사다리를 만났다면
                if graph[j][start-1] == 1:
                    start -= 1
                else:
                    start += 1
        if i != start:
            return False
    return True

def solve(graph, cnt):
    if checkresult(graph):
        return cnt
    if cnt == 4:
        return -1
    else:
        point = checkpoint(graph)
        for p in point:
            board = copy.deepcopy(graph)
            board[p[0]][p[1]] = 1
            board[p[0]][p[1]+1] = 1
            solve(board, cnt+1)

answer = 4


print(solve(graph,0))