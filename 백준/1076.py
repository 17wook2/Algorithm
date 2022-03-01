color = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
color_dict = {}
s = 1
for i in range(len(color)):
    color_dict[color[i]] = s
    s *= 10
q = []
for i in range(3):
    q.append(input())

ans = ''
k = 0
for i in range(3):
    if i == 2:
        k = int(ans)
        k *= color_dict[q[i]]
    else:
        ans += str(color.index(q[i]))

print(k)
