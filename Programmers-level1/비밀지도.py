# def solution(n, arr1, arr2):
#     result = []
#     for i in range(n):
#         result.append(format(arr1[i] | arr2[i], "b"))
#
#     for i in range(n):
#         result[i] = result[i].replace("0", " ")
#         result[i] = result[i].replace("1", "#")
#         while len(result[i]) < n:
#              result[i] = " " + result[i]
#
#     return result

def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer




print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))