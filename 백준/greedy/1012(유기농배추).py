from collections import deque
T = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
case = []
for x in range(T):
    [M,N,K] = list(map(int,input().split()))
    land = [[0 for _ in range(M)] for __ in range(N)]
    for _ in range(K):
        [w,q] = list(map(int,input().split()))
        land[q][w] = 1
    answer = 0
    for i in range(N):
        for j in range(M):
            # print(i,j)
            if land[i][j] == 0:
                continue
            else:
                answer += 1
                # print(i,j)
                deq = deque([])
                deq.append((i,j))
                land[i][j] = 0
                while deq:
                    x,y = deq.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx < 0 or ny < 0 or nx >= N or ny >= M or land[nx][ny] == 0:
                            continue
                        else:
                            land[nx][ny] = 0
                            deq.append((nx,ny))
    case.append(answer)
for k in case:
    print(k)