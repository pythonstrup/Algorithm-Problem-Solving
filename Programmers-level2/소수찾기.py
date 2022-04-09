# 내 풀이
def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    from itertools import permutations
    answer = []

    for i in range(1, len(numbers)+1):
        n = list(set(permutations(numbers, i)))
        for j in n:
            value = int("".join(j))
            if is_prime(value): answer.append(value)

    return len(set(answer))


# 다른 사람 풀이
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)

# 다른 사람 풀이2
# 재귀 사용primeSet = set()
# 정답이 이상하게 나온다?
primeSet = set()


def isPrime(number):
    if number in (0, 1):
        return False
    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def makeCombinations(str1, str2):
    if str1 != "":
        if isPrime(int(str1)):
            primeSet.add(int(str1))

    for i in range(len(str2)):
        makeCombinations(str1 + str2[i], str2[:i] + str2[i + 1:])


def solution(numbers):
    makeCombinations("", numbers)

    answer = len(primeSet)

    return answer

print(solution("17"))
print(solution("011"))