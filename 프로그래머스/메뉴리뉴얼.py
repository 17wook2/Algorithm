from itertools import combinations
def solution(orders, course):
    answer = []
    for c in course:
        course_dictionary = {}
        for order in orders:
            if len(order) < c:
                continue
            else:
                combi = combinations(order,c)
            for element in combi:
                element = list(element)
                element.sort()
                # print(element)
                temp = ''
                for e in element:
                    temp += e
                if temp not in course_dictionary: # 딕셔너리에 없다면
                    course_dictionary[temp] = 1
                else:
                    course_dictionary[temp] += 1
        # print(course_dictionary)
        course_list = list(zip(course_dictionary.keys(),course_dictionary.values()))
        course_list.sort(key = lambda x:x[1], reverse = True)
        max_value = 0
        for co in course_list:
            max_value = max(max_value,co[1])
        if max_value == 1:
            continue
        for co in course_list:
            if co[1] == max_value:
                temp = ''.join(co[0])
                answer.append(temp)
            else:
                break
    answer.sort()
    return answer