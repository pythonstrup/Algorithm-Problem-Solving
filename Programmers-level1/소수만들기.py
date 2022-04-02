import itertools

def prime_number(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    result = itertools.combinations(nums, 3)
    for i in result:
        i = list(i)
        if prime_number(sum(i)):
            print(f"{i}를 이용해서 {sum(i)}를 만들 수 있습니다.")
            answer += 1

    return answer

num1 = [1,2,3,4]
num2 = [1,2,7,6,4]
print(solution(num1))
print(solution(num2))