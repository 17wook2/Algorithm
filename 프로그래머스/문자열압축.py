def solution(s):
    length = []
    result = ''
    if len(s) == 1:
        return 1
    for cut in range(1,len(s)//2+1):
        count = 1
        tempStr = s[:cut]
        for i in range(cut,len(s),cut):
            if s[i:i+cut] == tempStr: #다음 문자열도 같다면
                count += 1
            else:
                if count == 1:
                    count = ''
                result += str(count) + tempStr
                tempStr = s[i:i+cut]
                count = 1
        if count == 1:
            count = ''
        result += str(count) + tempStr
        length.append(len(result))
        result = ''
    return min(length)
def rotate(key):
    m = len(key)
    result = [[0]*m for i in range(m)]
    for i in range(m):
        for j in range(m):
            result[j][m-1-i] = key[i][j]
    return result
print(rotate([[0, 0, 0], [1, 0, 0], [0, 1, 1]]))