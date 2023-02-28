tc = int(input())
for _ in range(tc):
    cnt = 1
    n,k,t,m = list(map(int,input().split()))
    board = [[0]*(k+1) for i in range(n+1)]
    recent = [-1]*(n+1)
    submit = [0]*(n+1)
    for j in range(m):
        t_id,p_number,score = list(map(int,input().split()))
        board[t_id][p_number] = max(board[t_id][p_number] , score)
        recent[t_id] = j
        submit[t_id] += 1
    t_score = sum(board[t])
    for i in range(1,n+1):
        if i == t: continue
        at_score = sum(board[i])
        if t_score < at_score:
            cnt += 1
        if t_score == at_score:
            if submit[t] > submit[i]:
                cnt += 1
            if submit[t] == submit[i]:
                if recent[t] > recent[i]:
                    cnt += 1
    print(cnt)