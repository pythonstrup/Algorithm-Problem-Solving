def solution(x):
    x = str(x)
    summary = sum([int(x[i]) for i in range(len(x))])
    return int(x) % summary == 0

# 모범답안
def Harshad(n):
    # n은 하샤드 수 인가요?
    return n % sum([int(c) for c in str(n)]) == 0

print(solution(10))
print(solution(11))
print(solution(12))
print(solution(13))
