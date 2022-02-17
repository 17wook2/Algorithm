import bisect
la = ['-','java','python','cpp']
lb = ['-','backend','frontend']
lc = ['-','junior','senior']
ld = ['-','pizza','chicken']

def solution(infos, query):
    info_array = [[] for i in range(110)]
    for info in infos:
        infs = info.split(" ")
        a,b,c,d = la.index(infs[0]),lb.index(infs[1]),lc.index(infs[2]),ld.index(infs[3])
        idx = 0
        for i in [a,0]:
            for j in [b,0]:
                for k in [c,0]:
                    for h in [d,0]:
                        idx = (h + 3*k + 9*j + 27*i)
                        info_array[idx].append(int(infs[4]))
    for i in range(108):
        info_array[i].sort()
    res = []
    for q in query:
        z = q.split(" ")
        a,b,c,d,e = la.index(z[0]),lb.index(z[2]),lc.index(z[4]),ld.index(z[6]),z[7]
        e = int(e)
        idx = d + 3*c + 9*b + 27*a
        res.append(len(info_array[idx]) - bisect.bisect_left(info_array[idx],e))
    return res