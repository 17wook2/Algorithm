n,l = list(map(int,input().split()))
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

def check(array):
    visited = [0 for i in range(n)] ## 지나갈 수 있는지 확인하기 위한 배열
    for i in range(n-1):
        if array[i] == array[i+1]:
            continue
        elif abs(array[i] - array[i+1]) >= 2:
            return False
        elif array[i] - array[i+1] == 1: ## 위의가 높은것이라면 오른쪽 확인
            temp = array[i+1]
            for j in range(i+1,i+1+l): ## 같은 높이가 L개 있는지 확인
                if 0 <= j < n:
                    if array[j] == temp and not visited[j]:
                        visited[j] = 1
                    else:
                        return False
                else:
                    return False
        elif array[i+1] - array[i] == 1:
            temp = array[i]
            for j in range(i,i-l,-1):
                if 0 <= j < n:
                    if temp == array[j] and not visited[j]:
                        visited[j] = 1
                    else:
                        return False
                else:
                    return False
    return True

def simulate():
    answer = 0
    for i in range(n):
        if check(arr[i]):
            answer += 1
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(arr[j][i])
        if check(temp):
            answer += 1
    print(answer)
simulate()


# print(check([2,1,1,1,1,2]))