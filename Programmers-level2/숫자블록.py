import math

def solution(begin, end):
    result = []
    for i in range(begin, end+1):
        if i == 1:
            result.append(0)
            continue

        # n*2 번째 위치부터 블록이 들어가므로 모든 소수는 1이 들어간다.
        # 하지만  10,000,000번 블록까지만 놓을 수 있다는 점을 생각해야한다.
        for j in range(2, int(math.sqrt(i)) + 1):
            if i // j > 10**7:
                continue
            if i % j == 0:
                result.append(i // j)
                break
        else:
            result.append(1)

    return result