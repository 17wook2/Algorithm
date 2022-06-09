def solution(n, s):
     if n > s:
         return [-1]
     k = s//n
     ans = [k]*n
     s = s % n
     idx = 0
     while s != 0:
         ans[idx] += 1
         idx += 1
         idx %= n
         s -= 1
     ans.sort()
     return ans