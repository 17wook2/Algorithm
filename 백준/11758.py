p = []
for i in range(3):
    p.append(list(map(int,input().split())))
def ccw(a,b,c):
    return a[0]*b[1] + b[0]*c[1] + c[0]*a[1] - (b[0]*a[1] + c[0]*b[1] + a[0]*c[1])
t = ccw(p[0],p[1],p[2])
if t > 0:
    print(1)
elif t < 0:
    print(-1)
else:
    print(0)