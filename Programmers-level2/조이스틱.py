
def solution(name):
    answer = 0
    cost = [min(ord(alp) - ord('A'), ord('Z') - ord(alp) + 1) for alp in name]
    idx = 0

    while True:
        answer += cost[idx]
        cost[idx] = 0
        if sum(cost) == 0:
            return answer

        left, right = 1, 1
        while cost[idx - left] == 0:
            left += 1
        while cost[idx + right] == 0:
            right += 1

        print(idx, left, right)
        answer += left if left < right else right
        idx += -left if left < right else right

    return answer

n = "JEROEN"
print(solution(n))

n = "JAN"
print(solution(n))

n = "ABABAABA"
print(solution(n))

n = "AAAABABAAAA"
print(solution(n))