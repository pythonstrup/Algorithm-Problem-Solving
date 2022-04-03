# 내 풀이
# def solution(s):
#     words = s.split(' ')
#     answer = []
#     for word in words:
#         result = ''
#         arr = list(word)
#         for i in range(len(arr)):
#             if i == 0:
#                 arr[i] = arr[i].upper()
#             else:
#                 arr[i] = arr[i].lower()
#
#         answer.append(''.join(arr))
#
#     return " ".join(answer)

# 다른 사람 풀이1
def solution(s):
    answer = ''
    for i in s.lower().split(' '):
        if answer == '':
            answer += i.capitalize() # upper로 쓸 수도 있음
        else:
            answer += ' '+i.capitalize()
    return answer

# 다른 사람 풀이2
# def solution(s):
#     return s.title()

print(solution("3people unFollowed me"))
print(solution("for the last week"))