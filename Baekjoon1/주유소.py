
# 내 풀이
# n = int(input())
# path = list(map(int, input().split()))
# city = list(map(int, input().split()))
#
# result = 0
# i = 0
# while True:
#     if i > n-2:
#         break
#     tmp = city[i]
#     result += path[i] * city[i]
#     while tmp < city[i+1]:
#         if i < n-2:
#             i += 1
#             result += tmp * path[i]
#     i += 1
#
# print(result)


# 모범 답안
n = int(input())
cities = list(map(int, input().split()))
prices = list(map(int, input().split()))

result = 0
min_prices = prices[0]

for i in range(n-1):
    if prices[i] < min_prices:
        min_prices = prices[i]

    result += min_prices * cities[i]

print(result)