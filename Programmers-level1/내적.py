# def solution(a, b):
#     result = 0
#     for x, y in zip(a, b):
#         result += x * y
#     return result


# 한 줄 코드
def solution(a, b):
    return sum([x*y for x, y in zip(a,b)])


a1 = [1,2,3,4]
a2 = [-3,-1,0,2]
b1 = [-1,0,1]
b2 = [1,0,-1]
print(solution(a1, a2))
print(solution(b1, b2))