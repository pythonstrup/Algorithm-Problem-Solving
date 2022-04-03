# 내 풀이

def solution(arr):
    answer = arr[0]
    for i in range(1, len(arr)):
        a = answer
        b = arr[i]
        while b > 1:
            if a < b:
                a, b = b, a

            if a % b == 0:
                break
            else:
                a = a % b
        answer = answer * arr[i] // b

    return answer


# 다른 사람 풀이
# from math import gcd
#
# def solution(num):
#     answer = num[0]
#     for n in num:
#         answer = n * answer // gcd(n, answer)
#
#     return answer


print(solution([2,6,8,14]))

print(solution([1,2,3]))