
n = int(input())
numbers = list(map(int, input().split()))
result = max(numbers) * min(numbers)

print(result)