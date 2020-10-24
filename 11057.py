N = int(input())
dp = [[0 for _ in range(10)] for _ in range(1001)]
for i in range(0, 10):
    dp[1][i] = 1
for i in range(2, N + 1):
    for j in range(10):
        if j == 9:
            dp[i][j] = dp[i - 1][9]
        else:
            for k in range(j, 10):
                dp[i][j] += dp[i - 1][k]
print(sum(dp[N]) % 10007)