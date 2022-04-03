# def solution(arr1, arr2):
#     answer = []
#
#     for i in range(len(arr1)):
#         result = []
#         for j in range(len(arr2[0])):
#             value = 0
#             for k in range(len(arr2)):
#                 value += arr1[i][k] * arr2[k][j]
#
#             result.append(value)
#         answer.append(result)
#
#     return answer

# 다른 사람풀이
def solution(A, B):
    return [[sum(a*b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))