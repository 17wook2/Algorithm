def solution(name):
    name_length = [min(ord(i) - ord('A'), ord('Z') - ord(i) +1) for i in name]
    answer = 0
    idx = 0
    while True:
        answer += name_length[idx]
        name_length[idx] = 0
        if sum(name_length) == 0: # 바꿀것이 없다면
            break
        else: # 왼쪽 또는 오른쪽
            left = 1
            right = 1
            while name_length[idx - left] == 0:
                left += 1
            while name_length[idx + right] == 0:
                right += 1
            answer += left if left < right else right
            idx -= left if left < right else -right  # 왼쪽으로 이동하면 left만큼 빼기
    return answer