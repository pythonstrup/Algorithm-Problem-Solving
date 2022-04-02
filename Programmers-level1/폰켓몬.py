# def solution(nums):
#     select = len(nums)//2
#     nums = list(set(nums))
#     answer = len(nums)
#     if select > answer:
#         return answer
#     else:
#         return select

def solution(nums):
    return min(len(set(nums)), len(nums)//2)



num1 = [3,1,2,3]
num2 = [3,3,3,2,2,4]
num3 = [3,3,3,2,2,2]

print(solution(num1))
print(solution(num2))
print(solution(num3))