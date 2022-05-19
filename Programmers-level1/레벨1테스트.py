def solution(s):
    answer = [i for i in s]
    answer.sort(reverse=True, key=lambda x: ord(x))
    return "".join(answer)

print(solution("Zbcdefg"))

def solution(nums):
    n = len(nums) // 2
    nums = list(set(nums))
    answer = len(nums) if n > len(nums) else n
    return answer

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))