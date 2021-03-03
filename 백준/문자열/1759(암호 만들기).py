from itertools import combinations
l,c = map(int,input().split())
array = list(input().split())
m = ['a','e','i','o','u']
candidate = list(combinations(array,l))
answer = []
for c in candidate:
    left = 0
    right = 0
    for x in c:
        if x in m:
            left += 1
        else:
            right += 1
    if left >= 1 and right >= 2:
        c = list(c)
        c.sort()
        answer.append(''.join(c))
answer.sort()
for ans in answer:
    print(ans)


