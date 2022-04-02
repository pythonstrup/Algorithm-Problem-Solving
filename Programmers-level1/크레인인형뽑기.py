def solution(board, moves):
    answer = 0
    stack = [-1, 0]
    for move in moves:

        for step in range(len(board)):
            if board[step][move-1] != 0:
                stack.append(board[step][move-1])
                board[step][move-1] = 0
                break

        if stack[-2] == stack[-1]:
            answer += 2
            stack.pop()
            stack.pop()


    return answer



board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
move = [1,5,3,5,1,2,1,4]

print(solution(board, move))