from itertools import combinations
def solution(numbers, target):
    answer = 0
    sum_numbers = sum(numbers)
    if sum_numbers == target: # 모두 더해야 하는경우
        return 1
    else:
        for num in numbers: # -가 1개
            if sum_numbers - 2*num == target:
                answer += 1
        for i in range(2,len(numbers)):
            combination = list(combinations(numbers,i))
            for comb in combination:
                if sum_numbers - 2*sum(list(comb)) == target:
                    answer += 1
    return answer