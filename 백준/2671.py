import re
arr = input()
p = re.compile('(100+1+|01)+')
m = p.fullmatch(arr)
if m == None:
    print("NOISE")
else:
    # print(m)
    start = m.start(); end = m.end()
    if start == 0 and end == len(arr):
        print("SUBMARINE")
    else:
        print("NOISE")
