# 내 풀이
def solution(brown, yellow):
    size = brown + yellow
    n = 1
    m = 1
    for i in range(1, brown//2 + 1):
        n = i
        if size % i == 0:
            m = size // i
        else:
            continue

        if (n-2) * (m-2) == yellow and n >= m:
            return [n, m]

# 다른 사람 풀이
# 둘레 길이를 이용한 문제 풀이
def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]

# 다른 사람 풀이 2
# 내 풀이와 논리가 비슷
def solution(brown, red):
    nm = brown + red
    for n in range(1, nm+1):
        if nm%n != 0:
            continue
        m = nm//n
        if (n-2)*(m-2) == red:
            return sorted([n, m], reverse = True)

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
print(solution(16, 8))