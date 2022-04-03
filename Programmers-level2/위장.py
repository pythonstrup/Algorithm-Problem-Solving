from itertools import combinations
from collections import Counter

def solution(clothes):
    answer = {}
    for i in clothes:
        if i[1] in answer: answer[i[1]] += 1
        else: answer[i[1]] = 1

    cnt = 1
    for i in answer.values():
        cnt *= (i+1)
    return cnt - 1

def solution2(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer


# def solution(clothes):
#     style_dict = {}
#
#     for tu in clothes:
#         style_dict[tu[1]] = 0
#     for tu in clothes:
#         style_dict[tu[1]] += 1
#
#     result = [i for i in style_dict.values()]
#
#     answer = 0
#     for i in range(len(result)):
#         answer += result[i]
#         for j in range(i+1, len(result)):
#             answer += result[i] * result[j]
#
#     return answer


# def solution(clothes):
#     style_dict = {}
#
#     for tu in clothes:
#         style_dict[tu[1]] = 0
#     for tu in clothes:
#         style_dict[tu[1]] += 1
#
#     answer = sum(i for i in style_dict.values())
#     result = 0
#     if len(style_dict) > 1:
#         for i in style_dict.keys():
#             if result == 0:
#                 result = style_dict[i]
#             else:
#                 result *= style_dict[i]
#
#     answer += result
#     return answer

# def solution(clothes):
#     answer = 0
#     style_dict = {}
#
#     for tu in clothes:
#         try:
#             style_dict[tu[1]].append(tu[0])
#         except KeyError:
#             style_dict[tu[1]] = [tu[0]]
#
#     for i in style_dict.keys():
#         print(len(style_dict[i]))
#
#     return answer


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"],
                ["green_turban", "headgear"], ["green_turban2", "headgear"],
                ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))