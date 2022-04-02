from math import sqrt, pow
def solution(n):
    return pow((sqrt(n)+1), 2) if sqrt(n)%1 == 0 else -1

print(solution(121))
print(solution(3))