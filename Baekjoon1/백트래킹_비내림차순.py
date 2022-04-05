
def dfs(start):
    if len(numbers) == m:
        print(*numbers)
        return

    for i in range(start, n+1):
        numbers.append(i)
        dfs(i)
        numbers.pop()

n, m = map(int, input().split())
numbers = []
dfs(1)