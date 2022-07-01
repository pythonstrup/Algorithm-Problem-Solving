# 아래 동적계획법은 시간 초과됨
def solution(n):
    dp = [0] * (n + 1)

    if n >= 1:
        dp[1] = 1
    if n >= 2:
        dp[2] = 1

    for i in range(3, n + 1):
        if i % 2 == 1:
            dp[i] = min(dp[i // 2] + 1, dp[i - 1] + 1)
        else:
            dp[i] = min(dp[i // 2], dp[i - 1] + 1)

    return dp[n]

# 내 풀이
# log n으로 해결해보자 : 아래 이진법으로 푸는 것과 거의 차이가 없긴하다.
# 대입 오버헤드로 인해 0.01ms 정도의 차이가 발생하는듯
def solution(n):
    answer = 0
    while n != 0:
        if n % 2 == 1:
            n -= 1
            answer += 1
        else:
            n //= 2

    return answer

# 다른 사람 풀이
# 이진법을 이용하면 아주 쉽게 풀 수 있었다.......
# 그래도 이진법으로 표현된 수를 선형탐색 하며 1의 개수를 세야하므로 O(log n)만큼 시간이 소모된다.
def solution(n):
    return bin(n).count('1')