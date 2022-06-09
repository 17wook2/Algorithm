answer = 0
def solution(n, rooks):
    def check(x,y):
        dx = [-1,1,1,-1]
        dy = [1,1,-1,-1]
        for k in range(1,n):
            for i in range(4):
                nx = x + dx[i]*k
                ny = y + dy[i]*k
                if 0 <= nx < n and 0 <= ny < 2*n:
                    if board[nx][ny] == 1:
                        return False
        return True
    def dfs(x):
        global answer
        if x == rooks:
            answer += 1
        for i in range(2*n):
            if arr[x][i]:
                if check(x,i):
                    board[x][i] = 1
                    dfs(x+1)
                    board[x][i] = 0
    arr = [[0]*(n*2) for i in range(n)]
    for i in range(n):
        for j in range(i+1):
            arr[i][n] = 1
            arr[i][n+j] = 1
            arr[i][n-j] = 1
    for row in arr:
        print(row)
    board = [[0]*(n*2) for i in range(n*2)]
    dfs(0)
    return answer

solution(3,2)
