
n = int(input())
stair = []
for i in range(n):
    stair.append(int(input()))

dp = [0] * (n+1)
dp[1] = stair[0]

for i in range(2, n+1):
    if i == 2:
        dp[i] = dp[i-1] + stair[i-1]
    else:
        dp[i] = max(dp[i-2]+stair[i-1], dp[i-3]+stair[i-2]+stair[i-1])


print(dp[n])


