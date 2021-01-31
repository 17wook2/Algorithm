N = int(input())
tree = []
answer = ''
for i in range(N):
    lst = list(map(int,input()))
    tree.append(lst)
def quadtree(x,y,n):
    if n == 1:
        return str(tree[x][y])
    result = []
    for i in range(x,x+n):
        for j in range(y,y+n):
            if tree[x][y] != tree[i][j]: # 분할
                result.append('(')
                result.extend(quadtree(x,y,n//2))
                result.extend(quadtree(x,y+n//2,n//2))
                result.extend(quadtree(x+n//2,y,n//2))
                result.extend(quadtree(x+n//2,y+n//2,n//2))
                result.append(')')
                return result
    return str(tree[x][y])
print(''.join(quadtree(0,0,N)))