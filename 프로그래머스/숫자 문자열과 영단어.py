def solution(s):
    answer = ''
    idx = 0
    alphabet = {}
    alphabet['zero'] = '0'
    alphabet['one'] = '1'
    alphabet['two'] = '2'
    alphabet['three'] = '3'
    alphabet['four'] = '4'
    alphabet['five'] = '5'
    alphabet['six'] = '6'
    alphabet['seven'] = '7'
    alphabet['eight'] = '8'
    alphabet['nine'] = '9'
    idx = 0
    for i in range(len(s)):
        if s[idx:i+1] in alphabet:
            answer += alphabet[s[idx:i+1]]
            idx = i+1
        if s[i].isdigit():
            answer += s[i]
            idx = i + 1
    return int(answer)