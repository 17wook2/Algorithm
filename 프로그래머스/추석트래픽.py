def solution(lines):
    timetable = []
    answer = 0
    for line in lines:
        timetable.append(TimeToMs(line))
    print(timetable)
    for time in timetable:
        answer = max(answer,getThrouput(timetable, time[0]))
        answer = max(answer,getThrouput(timetable, time[1]))
    return answer

def TimeToMs(line):
    line = line.split(' ')
    h,m,s = line[1].split(':')
    duration = line[2].split('s')
    duration = int(float(duration[0]) * 1000)
    h = int(h) * 60 * 60 * 1000
    m = int(m) * 60 * 1000
    s,ms = s.split('.')
    s = int(s) * 1000
    ms = int(ms)
    end = h+m+s+ms
    start = end - duration + 1
    return [start, end]

def getThrouput(timetable,start):
    end = start + 1000
    answer = 0
    for time in timetable:
        if not(time[1] < start or time[0] >= end):
            answer += 1
    return answer