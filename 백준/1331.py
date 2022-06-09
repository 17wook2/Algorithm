d = []
nl, nr = 0,0
fl,fr = 0,0
dx = [-1,-2,-2,-1,1,2,2,1]
dy = [-2,-1,1,2,2,1,-1,-2]
for i in range(36):
    x = input()
    l = ord(x[0])-65
    r = int(x[1])-1
    if i == 0:
        nl,nr = l,r
        fl,fr = l,r
        d.append((l,r))
        continue

    for j in range(8):
        nx = nl + dx[j]
        ny = nr + dy[j]
        if 0 <= nx < 6 and 0 <= ny < 6 and nx == l and ny == r and (nx,ny) not in d:
            d.append((nx,ny))
            nl,nr = l,r
            break
flag = False
for j in range(8):
    nx = nl + dx[j]
    ny = nr + dy[j]
    if 0 <= nx < 6 and 0 <= ny < 6 and nx == fl and ny == fr:
        flag = True

if len(d) < 36 or not flag:
    print("Invalid")
else:
    print("Valid")
