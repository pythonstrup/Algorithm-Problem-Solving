# import math
#
# def solution(n):
#     arr = [True] * (n+1)
#     answer = 0
#
#     for i in range(2, int(math.sqrt(n))+1):
#         if arr[i] == False:
#             continue
#
#         for j in range(i+i, n+1, i):
#             arr[j] = False
#
#     for i in range(2, n+1):
#         if arr[i] == True:
#             answer += 1
#
#     return answer

def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)



print(solution(10))
# print(solution(5))