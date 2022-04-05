import sys
input = sys.stdin.readline


n = int(input())
houses = []
for i in range(n):
    a, b, c = map(int, input().split())
    houses.append((a, b, c))

dp = [[0] * 4 for _ in range(n+1)]
for i in range(1, n+1):
    dp[i][1] = min(dp[i-1][2], dp[i-1][3]) + houses[i-1][0]
    dp[i][2] = min(dp[i-1][1], dp[i-1][3]) + houses[i-1][1]
    dp[i][3] = min(dp[i-1][1], dp[i-1][2]) + houses[i-1][2]


print(min(dp[n][1], dp[n][2], dp[n][3]))


# import sys
# input = sys.stdin.readline
#
#
# n = int(input())
# houses = []
# for i in range(n):
#     a, b, c = map(int, input().split())
#     houses.append((a, b, c))
#
# dp = [[0] * 4 for _ in range(n+1)]
# for j in range(1, n+1):
#     for i in range(1, 4):
#         value = houses[j-1][i-1]
#         if i == 1:
#             dp[j][i] = min(dp[j - 1][i+1], dp[j - 1][i+2]) + value
#         elif i == 2:
#             dp[j][i] = min(dp[j - 1][i - 1], dp[j - 1][i + 1]) + value
#         else:
#             dp[j][i] = min(dp[j - 1][i - 2], dp[j - 1][i - 1]) + value
#
# print(min(dp[n][1], dp[n][2], dp[n][3]))
