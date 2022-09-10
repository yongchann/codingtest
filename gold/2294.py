n, k = map(int, input().split())
coin = sorted(set([int(input()) for _ in range(n)]))
dp = [float("INF")] * (k+1)
dp[0] = 0
for i in range(1, k+1):
    for c in coin:
        if i < c:
            break
        dp[i] = min(dp[i], dp[i-c]+1)

print([dp[k], -1][dp[k]==float("INF")])