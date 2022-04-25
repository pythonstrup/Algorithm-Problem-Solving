# 내 풀이
def solution(numbers):
    compare = []

    for i in numbers:
        if i < 10:
            compare.append((str(i), str(i) * 4))
        elif 10 <= i < 100:
            compare.append((str(i), str(i) * 2))
        else:
            compare.append((str(i), str(i) + (str(i)[0])))

    compare.sort(reverse=True, key=lambda x: x[1])
    answer = ""
    for number in compare:
        answer += number[0]

    # 배열의 요소가 전부 0일 때 예외처리
    if answer.count('0') == len(answer):
        answer = "0"
    return answer


# 다른 사람 풀이
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))


# 다른 사람 풀이2
import functools


def comparator(a, b):
    t1 = a + b
    t2 = b + a
    return (int(t1) > int(t2)) - (int(t1) < int(t2))  # t1이 크다면 1  // t2가 크다면 -1  //  같으면 0


def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator), reverse=True)
    answer = str(int(''.join(n)))
    return answer


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([121, 12]))
print(solution([121, 0, 0, 2]))
print(solution([1000, 0, 0, 10]))
print(solution([0, 0, 0, 0]))