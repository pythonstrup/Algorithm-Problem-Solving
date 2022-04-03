
def solution(numbers, target):
    answer = 0
    n = len(numbers)

    def dfs(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx + 1, result + numbers[idx])
            dfs(idx + 1, result - numbers[idx])

    dfs(0, 0)
    return answer

# 내풀이
# def solution(numbers, target):
#     n = len(numbers)
#
#     global result
#     result = 0
#
#     def dfs(length, summary):
#         global result
#
#         if length == n:
#             if summary == target:
#                 result += 1
#         else:
#             dfs(length + 1, summary + numbers[length])
#             dfs(length + 1, summary - numbers[length])
#
#     dfs(0, 0)
#     return result

numbers = [1,1,1,1,1]
target = 3
print(solution(numbers, target))

numbers = [4, 1, 2, 1]
target = 4
print(solution(numbers, target))