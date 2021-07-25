from itertools import permutations
from collections import deque
import copy
import sys
input = sys.stdin.readline
n,m,d = list(map(int,input().split()))
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))
answer = 0
def count_enemy(x):
    enemy = 0
    for i in range(len(x)):
        for j in range(len(x[0])):
            if x[i][j] == 1:
                enemy += 1
    return enemy

archers = list(permutations(range(m),3))
directions = [(0,-1),(-1,0),(0,1)]

def get_distance(a,b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

for archer in archers:
    height = n
    board = copy.deepcopy(graph)
    enemy = count_enemy(board)
    while height != 0:
        ## board[height][e] 부터 시작
        stack = []
        queue = deque([])
        for e in archer:
            queue.append((height-1,e)) ## 거리
            while queue:
                x,y = queue.popleft()
                distance = get_distance((x,y),(height,e))
                if distance > d:
                    break;
                else:
                    if board[x][y] == 1 and distance <= d: ## kill한 적 담기
                        stack.append((x,y))
                        break
                    for direction in directions:
                        nx = x + direction[0]
                        ny = y + direction[1]
                        if 0 <= nx < n and 0 <= ny < m:
                            queue.append((nx,ny))
            queue.clear()
        for ele in stack:
            board[ele[0]][ele[1]] = 0
        height -= 1

        # print(stack)
    lived_enemy = count_enemy(board)
    answer = max(answer, enemy-lived_enemy)
print(answer)