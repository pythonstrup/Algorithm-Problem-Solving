# 성공! - 동적할당법
def solution(n):

    if n == 1:
        return 1
    elif n == 2:
        return 2

    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n] % 1234567


# 실패! 백트래킹으로 풀기에는 너무 많은 반복을 거쳐야 한다.
def solution(n):
    answer = []
    arr = [1] * n
    for i in range(n // 2): arr.append(2)

    length = len(arr)
    visited = [0] * length
    result = []

    def dfs():
        if sum(result) == n and result not in answer:
            answer.append(result[:])


        for i in range(length):
            if visited[i]:
                continue

            visited[i] = 1
            result.append(arr[i])
            dfs()
            result.pop()
            visited[i] = 0

    dfs()
    return len(answer)



print(solution(3))
print(solution(10))