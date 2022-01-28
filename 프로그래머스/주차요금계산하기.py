import math


def solution(fees, records):
    answer = []
    tmp = {}
    car_dict = {}
    for record in records:
        time, number, inout = record.split(' ')
        mtime = hmtomm(time)
        print(mtime)
        if number not in tmp or tmp[number] == -1:
            tmp[number] = mtime
        else:
            x = mtime - tmp[number]
            tmp[number] = -1
            if number not in car_dict:
                car_dict[number] = x
            else:
                car_dict[number] += x
    for key in tmp:
        if tmp[key] != -1:
            if key not in car_dict:
                car_dict[key] = 1439 - tmp[key]
            else:
                car_dict[key] += 1439 - tmp[key]

    d = sorted(car_dict)
    for k in d:
        answer.append(timetofee(fees, car_dict[k]))
    return answer


def hmtomm(time):
    h, m = time.split(':')
    hm = int(h) * 60
    m = int(m)
    return hm + m


def timetofee(fees, time):
    res = 0
    if fees[0] >= time:  ## 기본시간도 주차 안했다면
        return fees[1]
    res += fees[1]  ## 기본시간 초과
    x = time - fees[0]
    x /= fees[2]
    x = math.ceil(x)
    res += x * fees[3]
    print(res)
    return res