def solution(board):
    n = len(board)
    m = len(board[0])
    dp = board

    for i in range(1, n):
        for j in range(1, m):
            if dp[i][j] == 1:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

    answer = 0
    for i in range(n):
        result = max(dp[i])
        answer = max(answer, result)

    return answer**2


# 다른 사람 풀이
def findLargestSquare(board):
    answer = 1
    res = [[1 if x=='O' else 0 for x in y] for y in board]
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == 'O':
                res[y][x] = min(res[y-1][x], res[y-1][x-1], res[y][x-1]) + 1
                if res[y][x] > answer: answer = res[y][x]

    return answer ** 2


print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[0,0,1,1],[1,1,1,1]]))