# 내 풀이
# 아이디어를 떠올리지 못함....
# def solution(people, limit):
#     answer = 0
#     people.sort()
#
#     i = 0
#     j = len(people) - 1
#     while i <= j:
#         if limit >= people[i] + people[j]:
#             i += 1
#             j -= 1
#             answer += 1
#         else:
#             j -= 1
#             answer += 1
#
#     return answer

# 다른 사람 풀이
def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))