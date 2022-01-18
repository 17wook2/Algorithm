def solution(places):
    answer = []
    for place in places:
        answer.append(check(place))

    return answer

def check(place):
    array = []
    people = []
    for i in range(5):
        tmp = []
        for j in range(5):
            tmp.append(place[i][j])
            if place[i][j] == 'P':
                people.append((i,j))
        array.append(tmp)
    print(array)
    for p in people:
        result = dfs(array,p)
        if not result:
            return 0
    return 1
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def dfs(array,location):
    x,y = location
    stack = []
    stack.append((x,y,0))
    visited = []
    while stack:
        print(stack)
        x,y,cnt = stack.pop()
        visited.append((x,y))
        if cnt == 2:
            continue
        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < 5 and 0 <= ny < 5 and (nx,ny) not in visited:
                    if array[nx][ny] == 'P':
                        return 0
                    elif array[nx][ny] == 'O':
                        stack.append((nx,ny,cnt+1))
                        visited.append((nx,ny))
    return 1