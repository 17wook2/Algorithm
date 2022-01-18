import math
def solution(str1, str2):
    answer = 0
    arr1 = pause(str1)
    arr2 = pause(str2)
    return solve(arr1,arr2)

def pause(string):
    arr = []
    for i in range(len(string)-1):
        if string[i].isalpha() and string[i+1].isalpha():
            tmp = string[i] + string[i+1]
            tmp = tmp.lower()
            arr.append(tmp)
    return arr

def solve(arr1, arr2):
    isct = []
    tmp = list(set(arr1) & set(arr2)) # 교집합
    tmp2 = len(arr1) + len(arr2)
    for x in tmp:
        a = arr1.count(x)
        b = arr2.count(x)
        cnt1 = min(a,b)
        for i in range(cnt1):
            isct.append(x)
    tmp2 -= len(isct)
    if len(isct) == 0 and tmp2 == 0:
        return 65536
    ans = float(len(isct)) / float(tmp2)
    print(ans)
    ans *= 65536
    ans = math.trunc(ans)
    return ans