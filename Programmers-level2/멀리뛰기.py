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