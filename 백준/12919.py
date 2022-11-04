s = list(input())
t = list(input())
t = ''.join(t)
reversed_t = t[::-1]
ans = 0
def check(string):
    if string in t or string in reversed_t:
        return True
    else:
        return False

def solve(k):
    global ans
    if len(k) == len(t):
        if k == t:
            ans = 1
        return
    temp = k
    temp += 'A'
    if check(temp):
        solve(temp)
    temp = k
    temp += 'B'
    temp = temp[::-1]
    if check(temp):
        solve(temp)

solve(''.join(s))
print(ans)