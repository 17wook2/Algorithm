arr = list(input().split())
row = arr[0][1]
col = arr[0][0]
king = [8-int(row), int(ord(col))-65]
row = arr[1][1]
col = arr[1][0]
stone = [8-int(row), int(ord(col))-65]
n = int(arr[2])
query = []
dx = [0,0,1,-1,-1,-1,1,1]
dy = [1,-1,0,0,1,-1,1,-1]
dz = ['R','L','B','T','RT','LT','RB','LB']
for i in range(n):
    order = input()
    idx = dz.index(order)
    kx = king[0] + dx[idx]
    ky = king[1] + dy[idx]
    sx = stone[0] + dx[idx]
    sy = stone[1] + dy[idx]
    if 0 <= kx < 8 and 0 <= ky < 8:
        if kx == stone[0] and ky == stone[1]:
            if 0 <= sx < 8 and 0 <= sy < 8:
                stone[0] = sx
                stone[1] = sy
            else:
                continue
        king[0] = kx
        king[1] = ky


king_str = ''
king_str += str(chr(king[1] + 65))
king_str += str(8-king[0])
print(king_str)
stone_str = ''
stone_str += str(chr(stone[1] + 65))
stone_str += str(8-stone[0])
print(stone_str)