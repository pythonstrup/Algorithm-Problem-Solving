
def solution(array, commands):
    return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))


# def solution(array, commands):
#     answer = []
#     result = []
#     for i in commands:
#         result = array[i[0]-1:i[1]]
#         result.sort()
#         answer.append(result[i[2]-1])
#     return answer



arr = [1, 5, 2, 6, 3, 7, 4]
com = 	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(arr, com))