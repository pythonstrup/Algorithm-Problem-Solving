def solution(s):
    numbers = list(map(int, s.split()))
    answer = [str(min(numbers)), str(max(numbers))]

    return " ".join(answer)

print(solution("-1 -2 -3 -4"))