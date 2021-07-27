from collections import deque
n,m,k = list(map(int,input().split()))
food = [[5 for i in range(n)] for _ in range(n)] ## nxn
winter_food = []
trees = [[deque([]) for i in range(n)] for _ in range(n)]

for i in range(n):
    row = list(map(int,input().split()))
    winter_food.append(row)
for i in range(m):
    x,y,z = list(map(int,input().split()))
    trees[x-1][y-1].append(z)

def a():
    for i in range(n):
        for j in range(n):
            t = len(trees[i][j])
            for k in range(t):
                if food[i][j] >= trees[i][j][k]: ## 나이보다 양분이 많다면
                    food[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1
                else:
                    for q in range(k,t):
                        food[i][j] += trees[i][j].pop() // 2
                    break
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

def b():
    for i in range(n):
        for j in range(n):
            t = len(trees[i][j])
            for k in range(t):
                if trees[i][j][k] % 5 == 0:
                    for q in range(8):
                        nx = i + dx[q]
                        ny = j + dy[q]
                        if 0 <= nx < n and 0 <= ny < n:
                            trees[nx][ny].appendleft(1)
            food[i][j] += winter_food[i][j]

for i in range(k):
    a()
    b()

answer = 0
for i in range(n):
    for j in range(n):
        answer += len(trees[i][j])
print(answer)