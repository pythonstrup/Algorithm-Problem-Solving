# 내 풀이
def hanoi(n, fr, tmp, to, answer):
    if n == 1:
        answer.append([fr, to])
    else:
        hanoi(n-1, fr, to, tmp, answer)
        answer.append([fr, to])
        hanoi(n-1, tmp, fr, to, answer)

def solution(n):
    answer = []
    hanoi(n, 1, 2, 3, answer)
    return answer

# 다른 사람 풀이 1
def hanoi(n):

    def _hanoi(m, s, b, d):
        if m == 1:
            yield [s, d]
        else:
            yield from _hanoi(m-1, s, d, b)
            yield [s, d]
            yield from _hanoi(m-1, b, s, d)

    ans = list(_hanoi(n, 1, 2, 3))
    return ans  # 2차원 배열을 반환해 주어야 합니다.

# 다른 사람 풀이 2
def hanoi(f, t, m, n):
    if n == 0:
        return []

    return hanoi(f, m, t, n-1) + [[f, t]] + hanoi(m, t, f, n-1)


def solution(n):
    return hanoi(1, 3, 2, n)

print(solution(2))
print(solution(1))
print(solution(3))