
# def solution(arr1, arr2):
#     length = len(arr1[0])
#     for i in range(len(arr1)):
#         for j in range(length):
#             arr1[i][j] += arr2[i][j]
#
#     return arr1

def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer


arr1 =[[1,2],[2,3]]
arr2 =[[3,4],[5,6]]
print(solution(arr1, arr2))
