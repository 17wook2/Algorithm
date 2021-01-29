def solution(board):
    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
                if board[i][j] == 1:
                    board[i][j] = min(board[i][j-1],board[i-1][j-1],board[i-1][j]) + 1
    if sum(list(map(sum,board))) == 0:
        return 0
    return max(list(map(max,board)))**2