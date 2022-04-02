def solution(n):
    result = []
    while n >= 1:
        remainder = n % 3
        n //= 3
        result.append(remainder)

    result.reverse()
    answer = 0
    squared = 0
    for i in result:
        answer += i * (3**squared)
        squared += 1

    return answer

print(solution(45))
print(solution(229))