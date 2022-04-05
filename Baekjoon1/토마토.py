import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(q):
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if tomato[nx][ny] > 0 or tomato[nx][ny] == -1:
                continue

            tomato[nx][ny] = tomato[x][y] + 1
            q.append((nx, ny))

def print_result():
    result = 0
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 0:
                print(-1)
                return
        result = max(max(tomato[i]), result)

    print(result-1)

m, n = map(int, input().split())
tomato = []
for i in range(n):
    tomato.append(list(map(int, input().split())))

q = deque()
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append((i, j))

bfs(q)
print_result()

