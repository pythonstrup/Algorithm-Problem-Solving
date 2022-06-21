
# 내 풀이
import math

def solution(n, k):
    number = [i for i in range(1, n+1)]
    answer = []
    a = 1

    for i in range(1, n):
        b = math.factorial(n-i)

        index = int(k/b)
        k %= b
        # 만약 k%b 가 0이라면 인덱스에서 -1을 빼줘야 한다.
        if k == 0:
            index -= 1

        answer.append(number.pop(index))

    answer.append(number.pop())

    return answer


print(solution(3, 5))
print(solution(4, 11))
