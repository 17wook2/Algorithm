def solution(phone_book):
    dict = {number : 1 for number in phone_book}
    print(dict)
    for number in phone_book:
        for j in range(1,len(number)+1):
            try:
                if dict[number[:j]]: # 에러 발생하는 지점
                    print(dict[number[:j]])
                    if j == len(number):
                        continue
                    else:
                        return False
            except KeyError:
                continue
    return True