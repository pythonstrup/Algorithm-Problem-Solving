def solution(n):
    import itertools
    answer = [[1] * i for i in range(1,n+1)]

    row = -1; col = 0
    num = 1
    for i in range(n, 0, -3):
        for j in range(i):
            row += 1
            answer[row][col] = num
            num += 1
        for j in range(i-1):
            col += 1
            answer[row][col] = num
            num += 1
        for j in range(i-2):
            row -= 1
            col -= 1
            answer[row][col] = num
            num += 1

    return list(itertools.chain(*answer))

print(solution(4))
print(solution(5))
print(solution(6))