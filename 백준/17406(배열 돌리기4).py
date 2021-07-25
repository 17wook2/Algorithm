from itertools import permutations
import copy
import math
n,m,k = list(map(int,input().split()))
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))
rotations = []
for i in range(k):
    rotations.append(list(map(int,input().split())))
answer = math.inf
def do_rotate(graph,r,c,s):
    for i in range(1,s+1):
        left_top = graph[r-i][c-i]
        right_top = graph[r-i][c+i]
        left_bottom = graph[r+i][c-i]
        right_bottom = graph[r+i][c+i]
        for j in range(2*i):
            graph[r-i][c+i-j] = graph[r-i][c+i-j-1]
            graph[r+i-j][c+i] = graph[r+i-j-1][c+i]
            graph[r+i][c-i+j] = graph[r+i][c-i+j+1]
            graph[r-i+j][c-i] = graph[r-i+j+1][c-i]
        graph[r-i+1][c+i] = right_top
        graph[r+i][c+i-1] = right_bottom
        graph[r+i-1][c-i] = left_bottom
        graph[r-i][c-i+1] = left_top
    return graph

rotation_combination = list(permutations(range(k),k))
for r in rotation_combination:
    board = copy.deepcopy(graph)
    for e in r:
        board = do_rotate(board,rotations[e][0]-1,rotations[e][1]-1,rotations[e][2])
    for row in board:
        answer = min(answer,sum(row))

print(answer)