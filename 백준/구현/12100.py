import copy
n = int(input())
arr = []
for i in range(n):
    x = list(map(int,input().split()))
    arr.append(x)

def rotate(arr):
    ## 오른쪽으로 90도 돌리기
    arr2 = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            arr2[i][j] = arr[n-1-j][i]
    for i in range(n):
        for j in range(n):
            arr[i][j] = arr2[i][j]

def move(arr,d):
    ## d가 0 -> 왼쪽, 1-> 아래, 2->오른쪽, 3->위
    t = d
    while(d):
        rotate(arr)
        d -= 1
    for i in range(n):
        temp = [0] * n
        idx = 0
        for j in range(n):
            if arr[i][j] == 0:
                continue
            if temp[idx] == 0:
                temp[idx] = arr[i][j]
            elif temp[idx] == arr[i][j]:
                temp[idx] *= 2
                idx += 1
            else:
                idx += 1
                temp[idx] = arr[i][j]
        arr[i] = temp[:]
    while(4-t):
        rotate(arr)
        t += 1

def check(board):
    sol = 0
    for i in range(n):
        for j in range(n):
            sol = max(sol,board[i][j])
    return sol

answer = 0
for i in range(1024):
    array = []
    tmp = i
    for j in range(5):
        x = int(tmp % 4)
        array.append(x)
        tmp /= 4

    board = copy.deepcopy(arr)
    for e in array:
        move(board,e)
    answer = max(answer,check(board))

print(answer)
