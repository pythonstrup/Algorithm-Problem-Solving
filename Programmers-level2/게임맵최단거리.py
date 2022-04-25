def solution(maps):
    from collections import deque
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    n = len(maps)
    m = len(maps[0])

    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if maps[nx][ny] > 1 or maps[nx][ny] == 0:
                continue

            if nx == 0 and ny == 0:
                continue

            queue.append((nx, ny))
            maps[nx][ny] += maps[x][y]

    return maps[n-1][m-1] if maps[n-1][m-1] > 1 else -1


print(solution([[1,0,1,1,1],
                [1,0,1,0,1],
                [1,0,1,1,1],
                [1,1,1,0,1],
                [0,0,0,0,1]]))