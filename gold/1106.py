import sys
input = sys.stdin.readline
want, n = map(int, input().split())
info = sorted([list(map(int, input().split())) for _ in range(n)])
dp = [0] + [sys.maxsize] * (want+100)

for cost, client in info:
    for i in range(client, len(dp)):
        dp[i] = min(dp[i], dp[i-client] + cost)

print(min(dp[want:want+101]))

# 적어도 want 명을 얻을 수 있는 최소비용 
# dp[i] = i명의 고객을 얻기위한 최소 금액