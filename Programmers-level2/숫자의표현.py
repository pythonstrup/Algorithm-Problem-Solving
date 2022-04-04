# 내 풀이
# def solution(n):
#     answer = 0
#     for i in range(1, n+1):
#         result = 0
#         for j in range(i, n+1):
#             result += j
#             if result > n:
#                 break
#             elif result < n:
#                 continue
#             else:
#                 answer += 1
#                 break
#
#     return answer

# 다른 사람 풀이
# 내 풀이보다 효율적임
def solution(num):
    answer = 0
    for i in range(1, num + 1):
        s = 0
        while s < num:
            s += i
            i += 1
        if s == num:
            answer += 1
    return answer

# 다른 사람 풀이
# def solution(n):
#     return len([i for i in range(1, n + 1, 2) if n % i == 0])

print(solution(15))
print(solution(20))
