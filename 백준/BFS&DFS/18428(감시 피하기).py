from itertools import combinations
import copy
n = int(input())
classroom = [input().split() for i in range(n)]
stack = []
teacher = []
# 빈칸 담기
for i in range(n):
    for j in range(n):
        if classroom[i][j] == 'X':
            stack.append((i,j))
        elif classroom[i][j] == 'T':
            teacher.append((i,j))
# 가능한 조합 구하기 빈칸에서 3개 뽑기
candidate = list(combinations(stack,3))
def solution(candidate):
    dx = [-1, 1, 0, 0]  # 상하좌우
    dy = [0, 0, -1, 1]
    for cand in candidate:
        # 장애물 추가
        for e in cand:
            classroom[e[0]][e[1]] = 'o'
        ss = []
        for t in teacher:
            ss.append((t[0],t[1],4))
        studentnumber = 0
        while ss:
            x,y,d = ss.pop()
            if d == 4:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if classroom[nx][ny] == 'S':
                            studentnumber += 1
                        elif classroom[nx][ny] == 'o':
                            continue
                        elif classroom[nx][ny] == 'X':
                            ss.append((nx,ny,i)) # i값에 따라서 방향선택
            else:
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < n:
                    if classroom[nx][ny] == 'S':
                        studentnumber += 1
                    elif classroom[nx][ny] == 'o':
                        continue
                    elif classroom[nx][ny] == 'X':
                        ss.append((nx, ny, d))  # i값에 따라서 방향선택
        for e in cand:
            classroom[e[0]][e[1]] = 'X'
        if studentnumber == 0: # 걸린사람이 없다면
            return True
    # 모든 조합 다 해도 studentnumber 을 0으로 만드는 경우가 없을때
    return False
print('YES' if solution(candidate) else 'NO')


