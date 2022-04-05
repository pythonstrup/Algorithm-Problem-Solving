
# 백트래킹 설명: https://blog.encrypted.gg/732

def dfs():
    if len(number) == m:
        print(*number)

    for i in range(1, n+1):
        if visited[i]:
            continue

        visited[i] = True
        number.append(i)
        dfs()
        number.pop()
        visited[i] = False

n, m = map(int, input().split())
number = []
visited = [False] * (n+1)
dfs()

