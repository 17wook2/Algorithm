def solve(w,k):
    d = {}
    minimum = 10001
    maximum = -1
    for i in range(len(w)):
        if w[i] in d:
            d[w[i]].append(i)
        else:
            d[w[i]] = [i]
    for key,array in d.items():
        s = 0
        e = s + k - 1
        if len(array) < k:
            continue
        while e < len(array):
            length = array[e] - array[s] + 1
            minimum = min(minimum, length)
            maximum = max(maximum, length)
            s += 1; e+= 1;
    return minimum, maximum

t = int(input())
for i in range(t):
    w = input()
    k = int(input())
    minimum,maximum = solve(w,k)
    if minimum == -1 or maximum == -1:
        print(-1)
    else:
        print(minimum, maximum)