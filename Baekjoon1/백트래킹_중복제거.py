
def dfs(start):
    if len(numbers) == m:
        if len(numbers) == m:
            print(" ".join(map(str, numbers)))

    for i in range(start, n+1):
        if i not in numbers:
            numbers.append(i)
            dfs(i+1)
            numbers.pop()


n, m = map(int, input().split())
numbers = []
result = []
dfs(1)
