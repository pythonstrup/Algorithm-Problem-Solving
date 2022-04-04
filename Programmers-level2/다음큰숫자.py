# 후기
# list.count의 시간복잡도를 걱정했으나, 굳이 Counter를 쓸 필요가 없다.
# list.count()의 시간복잡도 O(n) = Counter의 시간복잡도 O(n)
# 프로그래머스에서 둘 다 돌려본 결과 list.count는 0.00ms~0.02ms
# Counter로는 0.02~0.06ms정도 걸린다.

from collections import Counter

def solution(n):
    answer = n
    standard = Counter(bin(n))
    while True:
        answer += 1
        s = bin(answer)
        result = Counter(s)

        if standard['1'] == result['1']:
            break

    return answer

print(solution(78))

# 다른 사람 풀이
def nextBigNumber(n):
    num1 = bin(n).count('1')
    while True:
        n = n + 1
        if num1 == bin(n).count('1'):
            break
    return n

#아래 코드는 테스트를 위한 출력 코드입니다.
print(nextBigNumber(78))
