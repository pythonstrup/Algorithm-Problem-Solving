# 내 풀이
# 최대 3.2ms
def solution(orders, course):
    from itertools import combinations
    from collections import Counter

    course_dict = []
    for c in course:
        menu = []
        for o in orders:
            for i in list(combinations(o, c)):
                menu.append("".join(sorted(list(i))))
        course_dict.append(Counter(menu))

    answer = []
    for dict in course_dict:
        tmp = 2
        for key, value in dict.most_common():
            if value >= tmp:
                tmp = value
                answer.append(key)
            else:
                break

    answer.sort()
    return answer


import collections
import itertools

# 다른 사람 풀이
# 2.45ms
def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))