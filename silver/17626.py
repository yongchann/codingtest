n = int(input())

dp = [0] + [float('INF')] * (n)
dp[1] = 1
for i in range(2, n+1):
    temp = 1
    while True:
        if temp**2 > i: break
        dp[i] = min(dp[i], dp[i-temp**2]+1)
        temp += 1

print(dp[-1])

