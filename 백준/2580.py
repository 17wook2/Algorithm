arr = []
for i in range(9):
    arr.append(list(map(int,input().split())))
blank = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            blank.append((i,j))
def go(idx):
    if idx == len(blank):
        for row in arr:
            print(*row)
        exit()
    candidate = [i for i in range(1,10)]
    x,y = blank[idx]
    row = arr[x]
    for ele in row:
        if ele in candidate:
            candidate.remove(ele)
    for i in range(9):
        if arr[i][y] in candidate:
            candidate.remove(arr[i][y])
    for i in range(3):
        for j in range(3):
            nx = (x//3)*3 + i
            ny = (y//3)*3 + j
            if arr[nx][ny] in candidate:
                candidate.remove(arr[nx][ny])
    for ele in candidate:
        arr[x][y] = ele
        go(idx+1)
        arr[x][y] = 0

go(0)