# def solution(a, b):
#     if a < b:
#         return sum([i for i in range(a, b+1)])
#     else:
#         return sum([i for i in range(b, a+1)])


def solution(a, b):
    if a > b:
        a, b = b, a
    return sum([i for i in range(a, b+1)])


print(solution(3, 5))