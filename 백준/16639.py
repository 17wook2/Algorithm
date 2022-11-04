def getValue(start,end):
    res = []
    for pivot in range(start,end):
        if op[pivot] == '+':
            res.append(board[start][pivot][0] + board[pivot+1][end][0])
            res.append(board[start][pivot][0] + board[pivot+1][end][1])
            res.append(board[start][pivot][1] + board[pivot+1][end][0])
            res.append(board[start][pivot][1] + board[pivot+1][end][1])
        elif op[pivot] == '-':
            res.append(board[start][pivot][0] - board[pivot+1][end][0])
            res.append(board[start][pivot][0] - board[pivot+1][end][1])
            res.append(board[start][pivot][1] - board[pivot+1][end][0])
            res.append(board[start][pivot][1] - board[pivot+1][end][1])
        else:
            res.append(board[start][pivot][0] * board[pivot+1][end][0])
            res.append(board[start][pivot][0] * board[pivot+1][end][1])
            res.append(board[start][pivot][1] * board[pivot+1][end][0])
            res.append(board[start][pivot][1] * board[pivot+1][end][1])
    return max(res), min(res)
N = int(input())
n = N // 2
expression = list(input())
num,op = [],[]
for idx,value in enumerate(expression):
    if idx % 2 == 0:
        num.append(int(value))
    else:
        op.append(value)
board = [[[0,0] for i in range(n+1)] for j in range(n+1)]

for offset in range(n+1):
    for start in range(n+1-offset):
        end = start + offset
        if start == end:
            board[start][end][0] = num[start]
            board[start][end][1] = num[start]
        else:
            max_value, min_value = getValue(start,end)
            board[start][end][0] = max_value
            board[start][end][1] = min_value


print(board[0][n][0])