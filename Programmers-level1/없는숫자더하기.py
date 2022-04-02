# def solution(numbers):
#     summary = 0
#     for i in range(10):
#         if not i in numbers:
#             summary += i
#     return summary
#


def solution(numbers):
    return 45 - sum(numbers)


mem1 = [1,2,3,4,6,7,8,0]
mem2 = [5,8,4,0,6,7,9]
print(solution(mem1))
print(solution(mem2))