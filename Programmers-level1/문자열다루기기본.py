# def solution(s):
#     answer = False
#     if len(s) == 4 or len(s) == 6:
#         if s.isdigit():
#             answer = True
#
#     return answer

def solution(s):
    return s.isdigit() and len(s) in [4, 6]

print(solution("12b34a"))