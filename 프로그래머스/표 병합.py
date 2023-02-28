def solution(commands):
    answer = []
    arr = [[''] * 51 for i in range(51)]
    reference = [[[-1, -1] for i in range(51)] for i in range(51)]
    for i in range(51):
        for j in range(51):
            reference[i][j][0] = i
            reference[i][j][1] = j
    def getRef(x, y):
        x = int(x);
        y = int(y)
        ref_x, ref_y = reference[x][y]
        if ref_x == x and ref_y == y:  ## Head인 경우
            return x, y
        else:
            return getRef(ref_x,ref_y)

    for command in commands:
        print(command)
        com = command.split(" ")
        if com[0] == "UPDATE":
            if len(com) == 4:
                r, c, value = com[1], com[2], com[3]
                r_ref, c_ref = getRef(r, c)
                arr[r_ref][c_ref] = value
            else:
                value1, value2 = com[1], com[2]
                for i in range(51):
                    for j in range(51):
                        if arr[i][j] == value1:
                            arr[i][j] = value2

        elif com[0] == "MERGE":
            r1, c1, r2, c2 = com[1], com[2], com[3], com[4]
            if r1 == r2 and c1 == c2: continue
            r1_ref, c1_ref = getRef(r1, c1)
            r2_ref, c2_ref = getRef(r2, c2)
            value = ''
            if arr[r1_ref][c1_ref] == '':
                value = arr[r2_ref][c2_ref]
            else:
                value = arr[r1_ref][c1_ref]

            lst = []
            ## r2,c2 에 병합된 셀 전부 바꿔줘야함
            for i in range(51):
                for j in range(51):
                    x, y = reference[i][j]
                    ref_x, ref_y = getRef(x, y)
                    if ref_x == r2_ref and ref_y == c2_ref:
                        lst.append((i, j))
            for x, y in lst:
                arr[x][y] = ''
                reference[x][y][0] = r1_ref
                reference[x][y][1] = c1_ref
            arr[r1_ref][c1_ref] = value
        elif com[0] == "UNMERGE":
            r, c = com[1], com[2]
            r_ref, c_ref = getRef(r, c)
            value = arr[r_ref][c_ref]
            arr[r_ref][c_ref] = ''
            lst = []
            for i in range(51):
                for j in range(51):
                    x, y = reference[i][j]
                    ref_x, ref_y = getRef(x, y)
                    if ref_x == r_ref and ref_y == c_ref:
                        lst.append((i, j))
            for x, y in lst:
                arr[x][y] = ''
                reference[x][y][0] = x
                reference[x][y][1] = y
            arr[int(r)][int(c)] = value
        elif com[0] == "PRINT":
            r, c = com[1], com[2]
            r_ref, c_ref = getRef(r, c)
            if arr[r_ref][c_ref] == '':
                answer.append("EMPTY")
            else:
                answer.append(arr[r_ref][c_ref])

    return answer
ㅂ

