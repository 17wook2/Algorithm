n = int(input())
curves = []
for _ in range(n):
    curves.append(list(map(int,input().split())))

board = [[0 for i in range(101)] for _ in range(101)]

dx = [1,0,-1,0]
dy = [0,-1,0,1]
def getcurve(x,y,d,g):
    board[x][y] = 1
    d_stack = [d]
    for i in range(g):
        temp = []
        for j in range(len(d_stack)-1,-1,-1):
            t = (d_stack[j] + 1) % 4
            temp.append(t)
        d_stack.extend(temp)
    for td in d_stack:
        x += dx[td]
        y += dy[td]
        board[x][y] = 1

for curve in curves:
    x,y,d,g = curve
    getcurve(x,y,d,g)

answer = 0
for i in range(100):
    for j in range(100):
        if board[i][j]:
            if board[i][j+1] and board[i+1][j] and board[i+1][j+1]:
                answer += 1

print(answer)

