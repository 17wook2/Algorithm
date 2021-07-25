from collections import deque
blade = {}
for i in range(1,5):
    blade[i] = deque((list(map(int,input()))))
k = int(input())
rotation = []
for i in range(k):
    rotation.append(list(map(int,input().split())))

def dfs_left(start,direction):
    if start < 1 or blade[start+1][6] == blade[start][2]:
        return
    if blade[start+1][6] != blade[start][2]:
        dfs_left(start-1, -direction)
        blade[start].rotate(direction)

def dfs_right(start,direction):
    if start > 4 or blade[start-1][2] == blade[start][6]:
        return
    if blade[start-1][2] != blade[start][6]:
        dfs_right(start+1, -direction)
        blade[start].rotate(direction)

for rotate in rotation:
    x, direction = rotate
    dfs_left(x-1,-direction)
    dfs_right(x+1,-direction)
    blade[x].rotate(direction)

answer = 0
for i in range(1,5):
    if blade[i][0] == 1:
        answer += 2**(i-1)

print(answer)
