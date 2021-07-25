import math
n = int(input())
exp = input()
nums = []
operator = []
for e in exp:
    if e.isdigit():
        nums.append(e)
    else:
        operator.append(e)
answer = -math.inf
def solve(idx,local_sum):
    global answer
    if idx == len(operator):
        answer = max(answer, int(local_sum))
        return local_sum
    ## 앞에 괄호를 묶는경우
    left = eval(local_sum + operator[idx] + nums[idx+1])
    left = str(left)
    solve(idx + 1, left)

    ## 뒤에 괄호를 묶는경우, 연산자 2개는 있어야함
    if idx + 1 < len(operator):
        _right = eval(nums[idx+1] + operator[idx+1] + nums[idx+2])
        right = eval(local_sum + operator[idx] + str(_right))
        right = str(right)
        solve(idx + 2, right)
solve(0,nums[0])
print(answer)

