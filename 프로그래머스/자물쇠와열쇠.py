def solution(key, lock):
    m = len(key)
    n = len(lock)
    new_lock = [[0]*(n*3) for i in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    for roatate in range(4):
        key = rotate(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock) == True:
                    return True
                else:
                    for i in range(m):
                        for j in range(m):
                            new_lock[x+i][y+j] -= key[i][j]
    return False

def check(lock):
    n = len(lock) // 3
    for i in range(n,2*n):
        for j in range(n,2*n):
            if lock[i][j] != 1:
                return False
    return True

def rotate(key):
    m = len(key)
    result = [[0]*m for i in range(m)]
    for i in range(m):
        for j in range(m):
            result[j][m-i-1] = key[i][j]
    return result